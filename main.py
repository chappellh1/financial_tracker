from expense import Expense
from budget import Budget
from incometracker import Incometracker

def main():
    # Sample data
    expense1 = Expense(50, "2023-12-01", "groceries", "Supermarket")
    

    income_tracker = Incometracker()
    
    while True:
        income = income_tracker.get_income_from_user()
        income_tracker.add_income(income)
        another = input("Add another income? (yes/no): ")
        if another.lower() != 'yes':
            break


    total = income_tracker.total_income()
    print(f"Total Income: {total}")

    # Create a budget and add an expense
    food_budget = Budget("groceries", 300)
    food_budget.add_expense(expense1)

    # Display budget details
    print(f"Budget for {food_budget.category}: {food_budget.limit}")
    print(f"Current total: {food_budget.current_total()}")


if __name__ == "__main__":
    main()