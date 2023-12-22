class Budget:
    def __init__(self, category, limit):
        self.category = category
        self.limit = limit
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def current_total(self):
        return sum(expense.amount for expense in self.expenses)