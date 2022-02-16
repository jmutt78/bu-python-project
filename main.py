from cmath import log
from decimal import Decimal
import csv

expenses = []
output_file = []
selection = 0
# income = Decimal(input('Please enter your monthly income -->'))

'''
TODO:
    - test for amount to be a decimal
    - test for amount to be a positive number
'''


def gather_exp():
    global expenses
    while True:
        expense_name = input('Enter the expense name -->')
        expense_category = input('Enter the expense category -->')
        expense_amount = input('Enter the expense amount -->')
        expense = {'name': expense_name,
                   'category': expense_category, 'amount': expense_amount}
        expenses.append(expense)
        choice = Decimal(
            input('Enter 1 to add more expenses or 0 to exit -->'))
        if choice == 0:
            break


'''
TODO:
    - get the file name from the user input 
    - check if the file exists
    - if the file exists, load the data from the file.
    - test the data for name, category, amount.
    - if it is missing one of them, throw an error with what's missing.
    - if the file does not exist, or after the data is loaded, prompt the user.
    - remove any expenses that are not a postive number
'''


def cvs_analyze():
    global expenses
    with open("test.csv", mode='r', encoding='utf-8-sig') as myfile:
        firstline = True
        for line in myfile:
            if firstline:
                mykeys = "".join(line.split()).split(',')
                firstline = False
            else:
                values = "".join(line.split()).split(',')
                print(values)
                expenses.append({mykeys[n]: values[n]
                                 for n in range(0, len(mykeys))})


'''
TODO:
    - the expenses and totals by category
    - the total expenses
    - the difference between the total and the expenses
'''


def analyze_expenses():
    global expenses
    if(len(expenses)):
        csv_columns = ['category', 'name', 'amount']
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
