# main.py
from income import Income

def main():
    print("Welcome to the Financial and Budget Tracker")

    # Get user input for income details
    amount = float(input("Enter the income amount: "))
    timeframe = input("Enter the income timeframe (e.g., Monthly, Weekly): ")
    state = input("Enter the state where the income was earned: ")
    source = input("Enter the source of the income (e.g., Job Title): ")

    # Create an Income object
    my_income = Income(amount, timeframe, state, source)

    # Save the income to the database
    db_path = 'my_finances.db'
    my_income.save_to_db(db_path)

    print("Income saved successfully.")

if __name__ == "__main__":
    main()
