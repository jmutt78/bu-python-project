import unittest
from analyser import ExpensesAnalyzer


class Test (unittest.TestCase):
    # setting up class object
    analyser = ExpensesAnalyzer(income=10000)
    # call to csv_analyze so that all the calculation are done
    # full path to test.csv needs to be given as input
    ExpensesAnalyzer.csv_analyze(analyser)

    # Test case 1 to test analyze_expenses function
    def test_analyze_expenses(self):
        result = self.analyser.analyze_expenses()
        self.assertEqual(result, 'Income: 10000\nTotal Expenses: 2100\nExpenses Difference: 7900')

    # Test case 2 to test reset function
    def test_reset(self):
        self.analyser.reset()
        self.assertEqual(self.analyser.expenses, [])


if __name__ == '__main__':
    unittest.main()
