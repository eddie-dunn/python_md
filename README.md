python_md
=========

Markdown to HTML doc generator, implemented in Python

Usage
-----

From running `make_docs.py --help`:

	usage: make_docs.py [-h] [-d DEST] [-s SRC] [-c CSS]

	Generate HTML from markdowndocuments.

	optional arguments:
	  -h, --help            show this help message and exit
	  -d DEST, --dest DEST  Destination folder for generated
	                        documentation,defaults to 'docs'.
	  -s SRC, --src SRC     Folder with markdown source files, defaults to current
	                        dir.
	  -c CSS, --css CSS     The css file to use for the generated docs, defaults
	                        to 'markdown.css'.

In other words, `python_md` will default to taking all markdown
files in the current directory, generate html files from them,
and stick the generated html into a subfolder called `docs`.

If .css-files are present it will move these into the `docs`-
folder as well. If one of the .css-files are named
'markdown.css', they will be used automatically, otherwise you
will need to specify the css-file to use with the `-c`-flag.

In addition, .jpg- and .png-files will be moved to the
`docs`-folder as well, in case you have images for you wish to
display in the generated html.
