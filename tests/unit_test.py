import unittest
from mock import patch, call

import make_docs

class Test1(unittest.TestCase):

    @patch('make_docs.argparse.ArgumentParser')
    def test1(self, mock_parser):
        """Just run parse_args to see that it doesnt crash"""
        args = make_docs.parse_args()
        self.assertTrue(args)
        self.assertTrue(mock_parser.called)

    @patch('os.listdir')
    def test_make_list(self, ls_mock):
        def side_effect(arg):
            return sorted(['pythonfile.py', 'pyfile.py', 'junk'])
        ls_mock.side_effect = side_effect

        mlist = make_docs.make_list('somedir', ['.py'])
        self.assertEqual(sorted(['pyfile.py', 'pythonfile.py']), mlist)
        self.assertNotIn('junk', mlist)

    @patch('make_docs.make_list')
    @patch('make_docs.shutil.copy2')
    def test_copy_files_shutil_calls(self, copy2,  make_list):
        def side_effect(*args):
            return ['filename1', 'filename2', 'filename3']
        make_list.side_effect = side_effect

        correct_calls = [
            call(u'folder/filename1', u'/tmp/unique/filename1'),
            call(u'folder/filename2', u'/tmp/unique/filename2'),
            call(u'folder/filename3', u'/tmp/unique/filename3')
        ]

        make_docs.copy_files(['.py'], 'folder', '/tmp/unique')

        self.assertEqual(copy2.call_count, 3)
        self.assertEqual(correct_calls, copy2.mock_calls)
