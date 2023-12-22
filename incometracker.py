from income import Income

class Incometracker:
        def __init__(self):
            self.incomes = []

        def add_income(self, income):
            self.incomes.append(income)

        def total_income(self):
            return sum(income.amount for income in self.incomes)
        
        def get_income_from_user(self):
            print("Enter income details:")
            amount = float(input("Amount: "))
            date = input("Date (YYYY-MM-DD): ")
            source = input("Source: ")
            description = input("Description: ")

            return Income(amount, date, source, description)
            

        