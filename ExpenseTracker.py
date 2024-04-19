def main():
    tracker = ExpenseTracker()

    print("Welcome to Daily Expense Tracker App feature-y!")

    while True:
        print("\nSelect an option:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        try:
            choice = input("Enter choice (1/2/3/4): ").strip() or "4"  # Default to option 4 if no input is provided
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
