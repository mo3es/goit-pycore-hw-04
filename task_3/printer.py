from colorama import Fore

""" It provides printing of passed entity of file structur.
    If entity is directory it`s printed in blue, 
    if file - in green with additional indentation 5 spaces
"""


def file_printer(entity, message: str, indent: int):
    text_color = Fore.GREEN if entity == "file" else Fore.BLUE
    indent = indent if entity != "file" else indent + 5
    print(f"{text_color}{' '* indent}{message}{Fore.RESET}")
