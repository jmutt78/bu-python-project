import csv
import os


class ExpensesAnalyzer:
    """ Class to represent an ExpensesAnalyzer

    Attributes:
        __total_expenses (int): total expenses. Private attribute.
        expenses (list): list of expenses.
        __expense_difference (int): difference between income and expenses. Private attribute.
        income (int): income. If the argument is not given, it will be taken from user input.

    Methods:
        __get_input: For taking input of positive integers. Private method.
        gather_exp: For gathering expenses.
        csv_analyze: For reading csv file and adding to expenses.
        analyze_expenses: For generating expense report.
        reset: For resetting expenses.
        __create_all_expenses_file: For creating a file of all expenses. Private method.
        __str__: For printing the object.
        __sub__: For calculating the difference between income and expenses.
        __add__: For adding two ExpensesAnalyzers.
        set_expense_difference: For setting the __expense_difference private variable.
        get_expense_difference: For getting the __expense_difference private variable.
    """

    # init method
    def __init__(self, income=None):
        self.__total_expenses = 0
        self.expenses = []  # list
        self.__expense_difference = 'Not yet calculated. Analyze expenses first'
        if income is None:
            self.income = self.get_income()
        else:
            self.income = income

    # private method
    def __get_input(self, question):
        """
        Args:
            question (str): question to be asked.
        """
        # try except block
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
            choice = self.__get_input(
                'Enter 1 to add more expenses or any other number to exit -->')
            if choice == 1:
                continue
            else:
                break

    # private method and output file
    def __create_all_expenses_file(self):
        csv_columns = {'category', 'name', 'amount'}  # set
        with open("expense_list.csv", "w") as expense_file:
            dict_writer = csv.DictWriter(expense_file, csv_columns)
            dict_writer.writeheader()
            dict_writer.writerows(self.expenses)

    def set_expense_difference(self, value):
        """
        Args:
            value (int): value to be set.
        """
        self.__expense_difference = value

    def get_expense_difference(self):
        return self.__expense_difference

    # input file
    def csv_analyze(self):
        filepath = input("Please enter filepath: ")

        # check if file exist and throw an error if it does not
        if os.path.exists(filepath):
            with open(filepath, mode='r', encoding='utf-8-sig') as file_in:
                csv_columns = ['category', 'name', 'amount']  # list
                reader = csv.DictReader(file_in)
                csv_dict = tuple(reader)  # tuple
                headers = reader.fieldnames
                # try except block
                try:
                    # iteration type(for)
                    for i in csv_dict:
                        i["amount"] = int(i["amount"])
                        # conditional(if)
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
            total_by_category = {}  # dictionary

            # calculating total amount against each category
            # iteration type(for)
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
            self.__expense_difference = self.__sub__()

            # add the difference, total and income to the total_by_category dictionary
            total_by_category['Total'] = self.__total_expenses
            total_by_category['Income'] = self.income
            total_by_category['Difference'] = self.__expense_difference

            # create a file of all expenses
            self.__create_all_expenses_file()

            # create a file of the total by category and income
            with open('expense_report.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                for key, value in total_by_category.items():
                    writer.writerow([key, value])
                csv_file.close()

            print(
                f'Success! Your expenses have analyzed.\nCheck your files for more information.\nHere is your breakdown:\n{self.__str__()}\n')

        else:
            print("No expenses to analyze")

        return self.__str__()

    def reset(self):
        self.expenses = []
        print("Success! Your expenses have been reset.")

    # magic method
    def __sub__(self):
        return (self.income - self.__total_expenses)

    # A and B are objects of class and A has expenses = [1, 2, 3], B has expenses = [4, 5, 6] then A + B will return [1, 2, 3, 4, 5, 6]
    # magic method
    def __add__(self, other):
        return self.expenses.append(other.expenses)

    # str magic method
    def __str__(self):
        return f'Income: {self.income}\nTotal Expenses: {self.__total_expenses}\nExpenses Difference: {self.__expense_difference}'
