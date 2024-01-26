#!/usr/bin/env python

# MIT
#
# Copyright (c) 2022 mpvQC developers
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import argparse
import sys
from pathlib import Path
from textwrap import dedent


class ArgumentValidator:
    _errors = []

    def validate_directory(self, directory: Path, *, name: str):
        if not directory.exists():
            self._errors.append(f'{name.capitalize()} {directory} does not exist')
        elif not directory.is_dir():
            self._errors.append(f'{name.capitalize()} {directory} is not a directory')

    def break_on_errors(self):
        if errors := self._errors:
            for error in errors:
                print(error, file=sys.stderr)
            sys.exit(1)


class ProjectFileGenerator:
    _files = []

    def __init__(self, root_dir: Path):
        self._root_dir = root_dir

    def glob_files(self):
        self._files = [path for path in self._root_dir.rglob('*') if path.is_file()]

    def make_files_relative(self):
        self._files = [path.relative_to(self._root_dir) for path in self._files]

    def sort_files(self):
        self._files = sorted(self._files)

    def generate_qrc_file(self, qrc_file: Path):
        files = "".join([f"<file>{file}</file>" for file in self._files])

        template = dedent(f"""<!DOCTYPE RCC><RCC version="1.0"><qresource>{files}</qresource></RCC>""").strip("\n")

        qrc_file.write_text(template, encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description='Create a json project file')
    parser.add_argument('--relative-to', type=str, required=True,
                        help='Root directory to look for files')
    parser.add_argument('--out-file', type=str, required=True,
                        help='Path of the qrc file to generate')
    run(parser.parse_args())


def run(args):
    root_dir = Path(args.relative_to).absolute()
    out_file = Path(args.out_file)

    validator = ArgumentValidator()
    validator.validate_directory(root_dir, name='Root directory')
    validator.break_on_errors()

    generator = ProjectFileGenerator(root_dir=root_dir)
    generator.glob_files()
    generator.make_files_relative()
    generator.sort_files()
    generator.generate_qrc_file(qrc_file=out_file)


if __name__ == '__main__':
    main()