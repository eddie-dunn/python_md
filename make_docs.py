#!/usr/bin/env python3

import os
import shutil
import markdown
import argparse

# Default options you may configure
SRCPATH = "."
DESTINATION = "docs"
MD_EXTENSIONS = [".md", ".markdown"]
EXTRAS = [".jpg", ".png", ".css"]

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
                        "current dir."))
    parser.add_argument('-c', '--css', default=CSS_FILE,
                        help=("The css file to use for the generated docs, "
                        "defaults to 'markdown.css'."))
    return parser.parse_args()


def make_list(folder, extension_list):
    return [f for f in os.listdir(folder) for extension in extension_list
            if f.endswith(extension)]


def generate_html(filename, source, destination, css):
    name, _ = os.path.splitext(filename)
    output_file = destination + "/" + name + ".html"
    print("Generating ", filename, "--> ", output_file)

    md_text = ""
    with open(filename, 'r') as infile:
        md_text = markdown.markdown(infile.read(), extensions=['toc'])

    css_style = '<link href="%s" rel="stylesheet"></link>' % css
    html = "<html>\n\n{0}\n{1}</html>\n".format(css_style, md_text)
    with open(output_file, 'w') as outfile:
        outfile.write(html)


def copy_files(file_extensions, destination):
    extra_files = make_list(SRCPATH, file_extensions)
    for filename in extra_files:
        output = destination + "/" + filename
        print("Copying ", filename, "--> ", output)
        shutil.copy2(filename, output)


def main():
    args = parse_args()

    source_path = args.src
    destination = args.dest
    css = args.css

    # Make sure we have our destination folder ready
    if not os.path.exists(destination):
        os.makedirs(destination)

    # Generate markdown files
    md_files = make_list(source_path, MD_EXTENSIONS)
    for filename in md_files:
        generate_html(filename, source_path, destination, css)

    # Add extra source files to docs folder
    copy_files(EXTRAS, destination)


if __name__ == '__main__':
    main()
