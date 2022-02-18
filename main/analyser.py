import csv
import os


class Expenses_analyzer:
    def __init__(self, income=None):
        self.__total_expenses = 0
        self.expenses = []
        self.__expense_difference = 'Not yet calculated. Analyze expenses first'
        if income is None:
            self.income = self.get_income()
        else:
            self.income = income

    # for taking input of positive integers
    def __get_input(self, question):
        while True:
            try:
                number = int(input(question))
                if number < 0:
                    raise ValueError
                break
            except ValueError:
                print("that's not a positive number. Try again: ")
            except:
                print("that's not an integer. Try again: ")
        return number

    def get_income(self):
        income = self.__get_input("Please enter your monthly income: ")
        return income

    def gather_exp(self):
        while True:
            expense_name = input('Enter the expense name -->')
            expense_category = input('Enter the expense category -->')
            expense_amount = self.__get_input('Enter the expense amount -->')
            expense = {'name': expense_name,
                       'category': expense_category, 'amount': expense_amount}
            self.expenses.append(expense)

            choice = int(
                input('Enter 1 to add more expenses or 0 to exit -->'))
            if choice == 0:
                break

    # To create file expenses file
    def __create_all_expenses_file(self):
        csv_columns = {'category', 'name', 'amount'}
        with open("expense_list.csv", "w") as expense_file:
            dict_writer = csv.DictWriter(expense_file, csv_columns)
            dict_writer.writeheader()
            dict_writer.writerows(self.expenses)

    # setter for private variable
    def set_expense_difference(self, value):
        self.__expense_difference = value

    # getter for private variable
    def get_expense_difference(self):
        return self.__expense_difference

    # reads file and try to convert amount column to integer and then adds to expenses
    def csv_analyze(self):
        filepath = input("Please enter filepath: ")

        # check if file exist and throw an error if it does not
        if os.path.exists(filepath):
            with open(filepath, mode='r', encoding='utf-8-sig') as file_in:
                csv_columns = ['category', 'name', 'amount']
                reader = csv.DictReader(file_in)
                csv_dict = list(reader)
                headers = reader.fieldnames
                try:
                    for i in csv_dict:
                        i["amount"] = int(i["amount"])
                        if (i["amount"] < 0):
                            raise ValueError
                    if sorted(headers) != sorted(csv_columns):
                        raise KeyError
                except ValueError:
                    print("Could not convert data to an integer.")
                    return False
                except KeyError:
                    print(
                        "Error: Your CSV file is not in the correct format. it must contain 'category', 'name', 'amount'")
                    return False
                else:
                    self.expenses.extend(csv_dict)
                    print('Success! Your expenses have been loaded.')
        else:
            print('Error: File path is not valid')
            return False
        return True

    def analyze_expenses(self):
        if len(self.expenses):
            # create a dictionary of categories and the total amount
            total_by_category = {}

            # calculating total amount against each category
            for i in self.expenses:
                if i["category"] not in total_by_category:
                    total_by_category[i["category"]] = i["amount"]
                else:
                    total_by_category[i["category"]] += i["amount"]

            # total all expenses
            self.__total_expenses = 0
            for i in self.expenses:
                self.__total_expenses += i["amount"]

            # calculate the difference between the total and the expenses
            self.__expense_difference = self.income - self.__total_expenses

            # add the difference, total and income to the total_by_category dictionary
            total_by_category['Total'] = self.__total_expenses
            total_by_category['Income'] = self.income
            total_by_category['Difference'] = self.__expense_difference

            # create a file of all expenses
            self.__create_all_expenses_file()

            # create a file of the total by category and income
            with open('total_by_category.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                for key, value in total_by_category.items():
                    writer.writerow([key, value])
                csv_file.close()

            print(
                'Success! Your expenses have analyzed.\nCheck your files for more information.')
        else:
            print("No expenses to analyze")

        return self.__str__()

    def reset(self):
        self.expenses = []
        print("Success! Your expenses have been reset.")

    # if two objects of the this class are added using '+' sign like 'A + B' then the expenses list of A is extended by
    # expenses list of B
    def __add__(self, other):
        return self.expenses.append(other.expenses)

    # returns about of class
    def __str__(self):
        return f'Income: {self.income}\nTotal Expenses: {self.__total_expenses}\nExpenses Difference: {self.__expense_difference}'
