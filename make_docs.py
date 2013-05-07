#!/usr/bin/env python

import os
import shutil
import markdown
import argparse


# Default options you may configure
SRCPATH = "."
DESTINATION = "docs"
MD_EXTENSION = [".md", ".markdown"]
EXTRAS = [".jpg", ".png", ".css"]

CSS_FILE = 'markdown.css'
CSS_STYLE = '<link href="%s" rel="stylesheet"></link>' % CSS_FILE
# More styles to be found here:
# https://github.com/jasonm23/markdown-css-themes


def parse_args():
    parser = argparse.ArgumentParser(description='Generate HTML from md.')
    parser.add_argument('-d', '--dest', default=DESTINATION,
                        help="destination folder for generated documentation")
    parser.add_argument('-s', '--src', default=SRCPATH,
                        help="folder with markdown source files")

    return parser.parse_args()


def make_list(folder, extension_list):
    return [f for f in os.listdir(folder) for extension in extension_list
            if f.endswith(extension)]


def generate_markdown(destination):
    md_files = make_list(SRCPATH, MD_EXTENSION)
    for filename in md_files:
        name, extension = os.path.splitext(filename)
        output = destination + "/" + name + ".html"

        print "Generating ", filename, "--> ", output
        markdown.markdownFromFile(input=filename, output=output,
                                  extensions=['toc'])
        # TODO Add flagged css injection for html files
        # inject css inside head for correct html
        with open(output, 'a') as infile:
            infile.write(CSS_STYLE)


def copy_files(file_extensions, destination):
    img_files = make_list(SRCPATH, file_extensions)
    for filename in img_files:
        output = destination + "/" + filename
        print "Copying ", filename, "--> ", output
        shutil.copy2(filename, output)


def main():
    args = parse_args()

    destination = args.dest

    # Make sure we have our destination folder ready
    if not os.path.exists(destination):
        os.makedirs(destination)

    # Generate markdown files
    generate_markdown(destination)

    # Add source extra source files to docs folder
    copy_files(EXTRAS, destination)


if __name__ == '__main__':
    main()
