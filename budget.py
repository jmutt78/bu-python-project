class Budget:
    def __init__(self, cvs_file):
        self.expenses = {}
        self.income = 0
        self.cvs_file = cvs_file
        self.self_output = []
