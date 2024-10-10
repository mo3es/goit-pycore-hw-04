import sys
"""
    file provides calculation of total payments and average salary by given text file that contain lines with data. Each line contains data of one employee and this employee salary, that separated by commas.
    To provide calculations, defined two functions:
    - total_salary - provide calculation by given file (path). Retrieving salary data providing by recall second functions from total_salary
    - get_salaries_from_fil - provide parsing of given file and extracting salaries to results list, which return to caller function
"""

# Calculation total payment and average salary
def total_salary(path: str) -> tuple[float, float]:
    salaries = get_salaries_from_file(path)
    total = sum(salaries)
    average_salary = total / len(salaries)
    return (total, average_salary)




# Generation a list of payments by parsing data from the supplied file
def get_salaries_from_file(path: str) -> list():
    salaries_list = list()
    try:
        with open(path, 'r', encoding='UTF-8') as text:
            for line in text:
                if not line:
                    continue
                salaries_list.append(float(line.split(',')[1]))
        return salaries_list
    except FileNotFoundError:
        print("Given filename does not found")
        sys.exit(-1)
