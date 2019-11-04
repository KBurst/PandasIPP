import pandas
import os


if __name__ == "__main__":
    file_name = os.path.abspath(os.path.join("..", "Data", 'IPPDatabase.xlsx'))
    excel_file = pandas.read_excel(file_name)
    excel_headers = pandas.read_excel(file_name, nrows=0)
    print(excel_file)
