from cmath import log
from decimal import Decimal
import csv
import os

expenses = []
output_file = []
selection = 0
# income = Decimal(input('Please enter your monthly income -->'))


def gather_exp():
    global expenses
    while True:
        expense_name = input('Enter the expense name -->')
        expense_category = input('Enter the expense category -->')
        goodinput = False
        while not goodinput:
            try:
                expense_amount = int(input('Enter the expense amount -->'))
                if expense_amount > 0:
                    goodinput = True
                    print("Success! Your expenses have been loaded")
                else:
                    print("that's not a positive number. Try again: ")
            except ValueError:
                print("that's not an integer. Try again: ")
        expense = {'name': expense_name,
                   'category': expense_category, 'amount': expense_amount}
        expenses.append(expense)
        choice = Decimal(
            input('Enter 1 to add more expenses or 0 to exit -->'))
        if choice == 0:
            break


'''
TODO:
    - error any expenses that are not a positive number
'''


def cvs_analyze():
    global expenses
    filepath = input("Please enter filepath: ")
    # check if file exist and throw an error if it does not
    if(os.path.exists(filepath)):
        with open(filepath, mode='r', encoding='utf-8-sig') as file_in:
            csv_columns = ['category', 'name', 'amount']
            reader = csv.DictReader(file_in)
            csv_dict = list(reader)
            headers = reader.fieldnames
            #  check that the csv file is in the correct format
            if sorted(headers) != sorted(csv_columns):
                print(
                    "Error: Your CSV file is not in the correct format. it must contain 'category', 'name', 'amount'")

            else:
                #  load the data from the csv file
                expenses.extend(csv_dict)
                file_in.close()
                print('Success! Your expenses have been loaded.')
    else:
        print('Error: File path is not valid')


'''
TODO:
    - the expenses and totals by category
    - the total expenses
    - the difference between the total and the expenses
'''


def analyze_expenses():
    global expenses
    if(len(expenses)):
        csv_columns = {'category', 'name', 'amount'}
        expense_file = open("expense_list.csv", "w")
        dict_writer = csv.DictWriter(expense_file, csv_columns)
        dict_writer.writeheader()
        dict_writer.writerows(expenses)
        expense_file.close()

    else:
        print("No expenses to analyze")


while selection == 0:
    option_1 = 'Enter 1 to add expense details'
    option_2 = 'Enter 2 to upload a cvs file'
    option_3 = 'Enter 3 to analyze the expenses'
    option_4 = 'Enter 4 to exit'
    message = int(
        input(f"{option_1}\n{option_2}\n{option_3}\n{option_4}\n --------> "))

    if message == 1:
        gather_exp()
    elif message == 2:
        cvs_analyze()
    elif message == 3:
        analyze_expenses()
    else:
        break


'''
TODO:
    - Migrate to OOP and use inheritance
    - Add a method to calculate the total expenses
    - Add a method to calculate the difference between the total and the expenses
    - Create Unit Tests
'''
