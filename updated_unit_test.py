class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, date, amount, description):
        if date not in self.expenses:
            self.expenses[date] = []
        self.expenses[date].append(
            {"amount": amount, "description": description})

    def view_expenses(self, date):
        if date not in self.expenses:
            return "No expenses for this date."

        expense_list = self.expenses[date]
        output = ""
        for i, expense in enumerate(expense_list, start=1):
            output += f"{i}. Amount: ${expense['amount']}, Description: {expense['description']}\n"

        return output

    def delete_expense(self, date, index):
        if date not in self.expenses:
            return "No expenses for this date."

        if index < 1 or index > len(self.expenses[date]):
            return "Invalid expense index."

        del self.expenses[date][index - 1]
