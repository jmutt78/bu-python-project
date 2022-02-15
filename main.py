# check for a file
# if a file exists, load the data from the file.
# test the data for name, category, data.
# if it is missing one of them, throw an error with what's missing.
# if the file does not exist, or after the data is loaded, prompt the user.
# store the data into an object in an array

# add all the expenses, and store the total as a variable
# store the difference of the total and the expenses
# write them in a file and also print them in a formatted way to the console.

# check for duplicate expenses
# give them a breakdown for their expenses in each category
# give them a breakdown of in a list of expenses

from decimal import Decimal
import csv

expenses = []
cvs_file = ''
output_file = []
option_1 = 'Enter 1 to add expense details'
option_2 = 'Enter 2 to upload a cvs file'
option_3 = 'Enter 3 to exit'
selection = 0
# income = Decimal(input('Please enter your monthly income -->'))


def cvs_analyze():
    global expenses
    expense = []
    with open("test.csv", mode='r', encoding='utf-8-sig') as myfile:
        firstline = True
        for line in myfile:
            if firstline:
                mykeys = "".join(line.split()).split(',')
                firstline = False
            else:
                values = "".join(line.split()).split(',')
                expense.append({mykeys[n]: values[n]
                               for n in range(0, len(mykeys))})
    expenses.append(expense)


def gather_exp():
    global expenses
    print(expenses)
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


while selection == 0:
    message = int(input(f"{option_1}\n{option_2}\n{option_3}\n --> "))
    if message == 1:
        gather_exp()
    elif message == 2:
        cvs_analyze()
    else:
        break
