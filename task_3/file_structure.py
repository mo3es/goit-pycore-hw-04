from pathlib import Path
import printer
import sys

"""
    It provides iteration by file tree structure, that lays after the path
    passed as argument. Thorought iteration it call printer method to output
    current file-tree entity and set counter of steps in deep for indentation setting.
    Before start the iteration, it cheks existing of given path.
"""


def file_tree(path: str):
    if not Path(path).exists():
        print("Incorrect path")
        sys.exit(-1)
    print_file_tree(path)


global indent
global counter
indent = 0
counter = 0


def print_file_tree(path: str):
    if Path(path).is_file():
        file = Path(path).name
        global indent
        global counter
        printer.file_printer("file", file, indent + 5 * counter)
        return
    elif Path(path).is_dir():
        counter = counter + 1
        file = Path(path).name
        printer.file_printer("dir", file, indent + 5 * counter)
        for items in Path(path).iterdir():
            print_file_tree(path / items)
        counter = counter - 1
