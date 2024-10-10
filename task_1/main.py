from pathlib import Path
from salary_handler import total_salary


path = input('Input path to file with salaries:  ')
file_path = path if Path(path).is_file() else './salaries.txt'
salaries = total_salary(file_path)
print(f'Total payment: {salaries[0]:.2f}, average salary: {salaries[1]:.2f}')