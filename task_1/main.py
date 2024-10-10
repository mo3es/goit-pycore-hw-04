from pathlib import Path
from salary_handler import total_salary


path = input('Input path to file with salaries:  ')
file_path = path if Path(path).is_file() else './salaries.txt'
total, average = total_salary(file_path)
print(f'Total payment: {total:.2f}, average salary: {average:.2f}')