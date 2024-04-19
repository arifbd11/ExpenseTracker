class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, date, amount, description):
        if date not in self.expenses:
            self.expenses[date] = []
        self.expenses[date].append(
            {"amount": amount, "description": description})

    def view_expenses(self, date):
        if date in self.expenses:
            print(f"Expenses on {date}:")
            for idx, expense in enumerate(self.expenses[date]):
                print(
                    f"{idx + 1}. Amount: ${expense['amount']}, Description: {expense['description']}")
        else:
            print("No expenses recorded for this date.")

    def delete_expense(self, date, index):
        if date in self.expenses and 0 < index <= len(self.expenses[date]):
            del self.expenses[date][index - 1]
            print("Expense deleted successfully.")
        else:
            print("Invalid index or no expenses recorded for this date.")


def main():
    tracker = ExpenseTracker()

    print("Welcome to Daily Expense Tracker App!")

    while True:
        print("\nSelect an option:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        try:
            # Default to option 4 if no input is provided
            choice = input("Enter choice (1/2/3/4): ").strip() or "4"
        except EOFError:
            choice = "4"  # Set choice to option 4 if an EOFError occurs

        if choice == '1':
            date = input("Enter date (e.g., YYYY-MM-DD): ")
            amount = float(input("Enter amount spent: $"))
            description = input("Enter description: ")
            tracker.add_expense(date, amount, description)
            print("Expense added successfully.")
        elif choice == '2':
            date = input("Enter date to view expenses (e.g., YYYY-MM-DD): ")
            tracker.view_expenses(date)
        elif choice == '3':
            date = input(
                "Enter date of expense to delete (e.g., YYYY-MM-DD): ")
            index = int(input("Enter index of expense to delete: "))
            tracker.delete_expense(date, index)
        elif choice == '4':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a valid choice.")


if __name__ == "__main__":
    main()
