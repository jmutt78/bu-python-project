import unittest
from ExpensesAnalyzer import ExpensesAnalyzer


class Test (unittest.TestCase):
    """ Class to represent a Unit Test for ExpensesAnalyzer class.

    Methods:
    test_analyze_expenses: for testing analyze_expenses function.
    test_reset: for testing reset function.
    """
    # setting up class object
    analyser = ExpensesAnalyzer(income=10000)
    # call to csv_analyze so that all the calculation are done
    # full path to test.csv needs to be given as input
    ExpensesAnalyzer.csv_analyze(analyser)

    # unit test 1 for analyze_expenses function
    def test_analyze_expenses(self):
        result = self.analyser.analyze_expenses()
        self.assertEqual(
            result, 'Income: 10000\nTotal Expenses: 2100\nExpenses Difference: 7900')

    # unit test 2 for reset function
    def test_reset(self):
        self.analyser.reset()
        self.assertEqual(self.analyser.expenses, [])


if __name__ == '__main__':
    unittest.main()
