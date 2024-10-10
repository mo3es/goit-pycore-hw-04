import sys
import json

"""
    It provides processing of cat`s information by given text file that contain lines with data. Each line contains data of cat`s ID, name and age, that separated by commas.
    To provide processings, defined one function:
    - get_cats_info - provide parsing of given file and extracting cat`s datas, which return to caller programm as list of dictionaries and save it as json file
"""


def get_cats_info(path: str) -> list():
    cats = list()
    try:
        with open(path, "r", encoding="UTF-8") as text:
            for line in text:
                if not line:
                    continue
                id, name, age = line.strip().split(',')
                cats.append({"id": id, "name": name, "age": age})
        with open('cats.json', 'w', errors=None) as result:
            result.write(json.dumps(cats))
        return cats
    except FileNotFoundError:
        print("Given filename does not found")
        sys.exit(-1)
