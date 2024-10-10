from pathlib import Path
from salary_parser import total_salary
"""
    It`s entry-point that request from user path to file with employees data and call function total_salary to retrieve data from file and calculate total and average salary. Result is printed to console
"""

path = input("Input path to file with salaries:  ")
file_path = path if Path(path).is_file() else "./salaries.txt"
total, average = total_salary(file_path)
print(f"Total payment: {total:.2f}, average salary: {average:.2f}")
