import csv

def main():
    expenses = []
    print("Hello, welcome to the expense tracker!")
    while True:
        action = input("Choose your action: add/view/save/quit: ").lower()
        if action == "add":
            category = input("Category: ")
            amount = float(input("Amount: "))
            date = input("Date (YYYY-MM-DD): ")
            add_expense(expenses, category, amount, date)
        elif action == "view":
            summary = track_expenses(expenses)
            print("Expense Summary:", summary)
        elif action == "save":
            save_csv(expenses)
            print("Expenses saved to expense_tracker.csv")
        elif action == "quit":
            print("Thank you for using the expense tracker, have a great day!")
            break
        else:
            print("Invalid input, please enter a valid option")
            continue



def add_expense(expenses, category, amount, date):
    expense = {"category": category, "amount": amount, "date": date}
    expenses.append(expense)
    return expenses


def track_expenses(expenses):
    track = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        track[category] = track.get(category, 0) + amount
    return track


def save_csv(expenses):
    with open("expense_tracker.csv", "w", newline = "") as csvfile:
        headers = ["category" , "amount" , "date"]
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)


if __name__ == "__main__":
    main()