
import csv
import os

expenses = []
output_file = []
selection = 0
while True:
    try:
        income = int(input("Please enter your monthly income: "))
        if(income < 0):
            raise ValueError
        break
    except ValueError:
        print("Invalid Income. Try again: ")


def gather_exp():
    global expenses
    while True:
        expense_name = input('Enter the expense name -->')
        expense_category = input('Enter the expense category -->')
        test_input = False
        while not test_input:
            try:
                expense_amount = int(input('Enter the expense amount -->'))
                if expense_amount > 0:
                    test_input = True
                    print("Success! Your expenses have been loaded")
                else:
                    print("that's not a positive number. Try again: ")
            except ValueError:
                print("that's not an integer. Try again: ")
                break
        expense = {'name': expense_name,
                   'category': expense_category, 'amount': expense_amount}
        expenses.append(expense)
        choice = int(
            input('Enter 1 to add more expenses or 0 to exit -->'))
        if choice == 0:
            break


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
            try:
                for i in csv_dict:
                    i["amount"] = int(i["amount"])
                    if(i["amount"] < 0):
                        raise ValueError
                if sorted(headers) != sorted(csv_columns):
                    raise KeyError
            except ValueError:
                print("Could not convert data to an integer.")
                file_in.close()
            except KeyError:
                print(
                    "Error: Your CSV file is not in the correct format. it must contain 'category', 'name', 'amount'")
                file_in.close()
            else:
                expenses.extend(csv_dict)
                file_in.close()
                print('Success! Your expenses have been loaded.')
    else:
        print('Error: File path is not valid')


def analyze_expenses():
    if(len(expenses)):
        # create a dictionary of categories and the total amount
        total_by_category = {}
        for i in expenses:
            if i["category"] not in total_by_category:
                total_by_category[i["category"]] = i["amount"]
            else:
                total_by_category[i["category"]] += i["amount"]
        # total all expenses
        total_expenses = 0
        for i in expenses:
            total_expenses += i["amount"]
        # calculate the difference between the total and the expenses
        expense_difference = income - total_expenses
        # add the difference, total and income to the total_by_category dictionary
        total_by_category['Total'] = total_expenses
        total_by_category['Income'] = income
        total_by_category['Difference'] = expense_difference

        # create a file of all expenses
        csv_columns = {'category', 'name', 'amount'}
        expense_file = open("expense_list.csv", "w")
        dict_writer = csv.DictWriter(expense_file, csv_columns)
        dict_writer.writeheader()
        dict_writer.writerows(expenses)

        # create a file of the total by category and income
        with open('total_by_category.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in total_by_category.items():
                writer.writerow([key, value])
            csv_file.close()

        expense_file.close()
        print(
            'Success! Your expenses have analyzed.\nCheck your files for more information.')
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
    - Create Unit Tests
'''
