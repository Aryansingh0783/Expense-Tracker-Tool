class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, name, amount, category):
        expense = Expense(name, amount, category)
        self.expenses.append(expense)

    def view_expenses(self):
        total_expenses = 0
        print("Expense List:")
        for idx, expense in enumerate(self.expenses, 1):
            print(f"{idx}. {expense.name} - ${expense.amount} ({expense.category})")
            total_expenses += expense.amount
        print(f"Total Expenses: ${total_expenses}")

    def filter_expenses_by_category(self, category):
        filtered_expenses = [expense for expense in self.expenses if expense.category == category]
        total_expenses = sum(expense.amount for expense in filtered_expenses)
        print(f"Expenses under category '{category}':")
        for idx, expense in enumerate(filtered_expenses, 1):
            print(f"{idx}. {expense.name} - ${expense.amount}")
        print(f"Total Expenses under category '{category}': ${total_expenses}")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter Expenses by Category")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter expense name: ")
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            tracker.add_expense(name, amount, category)
            print("Expense added successfully!")
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            category = input("Enter category to filter: ")
            tracker.filter_expenses_by_category(category)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
