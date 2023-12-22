class Income:
    def __init__(self, amount, date, source, description):
        self.amount = amount
        self.date = date
        self.source = source
        self.description = description
    
    def get_income_from_user():
        print("Enter income details:")
        amount = float(input("Amount: "))
        date = input("Date (YYYY-MM-DD): ")
        source = input("Source: ")
        description = input("Description: ")
        return Income(amount, date, source, description)
