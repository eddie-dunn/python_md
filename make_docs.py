#!/usr/bin/env python

import os
import shutil
import markdown
import sys

SRCPATH = "."
# TODO Implement proper command parser
try:
    DESTINATION = sys.argv[1] + "/"
except IndexError:
    DESTINATION = "docs/"

MARKDOWN = "markdown2"
MD_EXTENSION = [".md", ".markdown"]
IMG_EXTENSION = [".jpg", ".png"]
EXTRAS = IMG_EXTENSION + [".css"]
GENERATED = [".html"] + IMG_EXTENSION

CSS_FILE = 'markdown.css'
CSS_STYLE = '<link href="%s" rel="stylesheet"></link>' % CSS_FILE
# More styles to be found here:
# https://github.com/jasonm23/markdown-css-themes


def make_list(folder, extension_list):
    return [f for f in os.listdir(folder) for extension in extension_list
            if f.endswith(extension)]

if not os.path.exists(DESTINATION):
    os.makedirs(DESTINATION)

# md_files = [f for f in listdir(SRCPATH) if valid_extension(f, MD_EXTENSION)]
md_files = make_list(SRCPATH, MD_EXTENSION)
for filename in md_files:
    name, extension = os.path.splitext(filename)
    output = DESTINATION + name + ".html"
    tmp_output = output + '.tmp'
    print "Generating ", filename, "--> ", output
    markdown.markdownFromFile(input=filename, output=output,
                              extensions=['toc'])
    # TODO Add flagged css injection for html files
    # inject css inside head for correct html
    with open(output, 'a') as infile:
        infile.write(CSS_STYLE)

# Add source extra source files to docs folder
img_files = make_list(SRCPATH, EXTRAS)
for filename in img_files:
    output = DESTINATION + filename
    print "Copying ", filename, "--> ", output
    shutil.copy2(filename, output)
