from pathlib import Path
from cat_parser import get_cats_info
"""
    It`s entry-point that request from user path to file with cat`s data and call function get_cats_info to retrieve data from file. Result of file parsing is printed to console
"""

path = input("Input path to file with cats info:  ")
file_path = path if Path(path).is_file() else "./cats.txt"
cats_info = get_cats_info(file_path)
print(cats_info)
