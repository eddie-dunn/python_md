#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

import os
import shutil
import markdown
import argparse
import codecs

# Default options you may configure
SRCPATH = "src"
DESTINATION = "docs"
MD_FILES = [".md", ".markdown"]
EXTRA_FILES = [".jpg", ".png", ".css"]

GENERATE_MARKDOWN_EXTENSIONS = [
    'toc',
    'tables',
    'codehilite(force_linenos=False,guess_lang=False)'
]

CSS_FILE = 'markdown.css'
# More styles to be found here:
# https://github.com/jasonm23/markdown-css-themes


def parse_args():
    parser = argparse.ArgumentParser(description=('Generate HTML from markdown'
        'documents.'))
    parser.add_argument('-d', '--dest', default=DESTINATION,
                        help=("Destination folder for generated documentation,"
                         "defaults to '%s'." % DESTINATION))
    parser.add_argument('-s', '--src', default=SRCPATH,
                        help=("Folder with markdown source files, defaults to "
                        "'%s'." % SRCPATH))
    parser.add_argument('-c', '--css', default=CSS_FILE,
                        help=("The css file to use for the generated docs, "
                        "defaults to 'markdown.css'."))
    return parser.parse_args()


def make_list(folder, extension_list):
    return [f for f in os.listdir(folder) for extension in extension_list
            if f.endswith(extension)]


def generate_html(filename, source, destination, css):
    filepath = "{}/{}".format(source, filename)

    name, _ = os.path.splitext(filename)
    output_file = "{}/{}.html".format(destination, name)
    print("Generating ", filepath, "--> ", output_file)
    md_text = ""
    with codecs.open(filepath, 'r', 'utf-8') as infile:
        md_text = markdown.markdown(infile.read(), extensions=['toc'])

    css_style = '<link href="%s" rel="stylesheet"></link>' % css
    html = "<html>\n\n{0}\n{1}</html>\n".format(css_style, md_text)
    with codecs.open(output_file, 'w', 'utf-8') as outfile:
        outfile.write(html)

def copy_files(file_extensions, source, destination):
    img_files = make_list(source, file_extensions)
    for filename in img_files:
        output_file = destination + "/" + filename
        input_file = "%s/%s" % (source, filename)

        print "Copying ", input_file, "--> ", output_file
        shutil.copy2(input_file, output_file)


def main():
    args = parse_args()

    source_path = args.src
    destination = args.dest
    css = args.css

    # Make sure we have our destination folder ready
    if not os.path.exists(destination):
        os.makedirs(destination)

    # Generate markdown files
    md_files = make_list(source_path, MD_FILES)
    for filename in md_files:
        generate_html(filename, source_path, destination, css)

    # Add extra necessary source files to docs folder
    copy_files(EXTRA_FILES, source_path, destination)


if __name__ == '__main__':
    main()
