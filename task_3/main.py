import sys
from pathlib import Path
from file_structure import file_tree

"""
    It sets default directory as parent directory and after checks
    correctness of given arguments. If path doesn`t passed as argument
    it use default.
    After performing path-checking, it calls function "file_tree()" for
    file-tree iteration
"""


start_path = Path.cwd().parent
if len(sys.argv) != 2:
    print(
        "Incorrect file recall. Usage: ./main.py path_to_needed_directory.  Directory chosen by default"
    )
else:
    start_path = sys.argv[1]

if Path(start_path).exists:
    file_tree(start_path)
else:
    print("Given path does not exist")
