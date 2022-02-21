"""
Justin McIntosh
Class: CS 521 - Spring 1
Date: 2/25/2022
Term Project

Runing the program:
* Run the application from main.py.
* When prompted, enter your income. Alternatively, you add your income as a argument.
  * EG: analyser_obj = Expenses_analyzer(income=10000)
* Choose the option that you want to perform. 
* To Close the application choose option 5.
* Note: If you want to upload a csv file, the file must be in the root directory of the project.

Unit Testing:
Run the application from UnitTests.py
You must use the test.csv file to test the application.
"""


from ExpensesAnalyzer import ExpensesAnalyzer

if __name__ == '__main__':
    # creating object of expenses_analyser class
    # if the income value given to __init__ if not given it will take input
    analyser_obj = ExpensesAnalyzer()

    #  user-defined function that accepts parameters/arguments and/or returns a value.
    def get_input(question):
        while True:
            try:
                number = int(input(question))
                if number <= 0 or number >= 6:
                    raise ValueError
                break
            except ValueError:
                print("Thats not a valid option. Try again: ")
        return number
    # try except block
    while True:
        option_1 = 'Enter 1 to add expense details'
        option_2 = 'Enter 2 to upload a cvs file'
        option_3 = 'Enter 3 to analyze the expenses'
        option_4 = 'Enter 4 to reset the expenses'
        option_5 = 'Enter 5 to quit the application'

        question = f"{option_1}\n{option_2}\n{option_3}\n{option_4}\n{option_5}\n\nPlease select an option: "
        message = get_input(question)

        if message == 1:
            analyser_obj.gather_exp()
        elif message == 2:
            analyser_obj.csv_analyze()
        elif message == 3:
            analyser_obj.analyze_expenses()
        elif message == 4:
            analyser_obj.reset()
        else:
            break
