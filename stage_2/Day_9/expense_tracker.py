# main.py

import json
import os
from datetime import datetime

DATA_FILE = "data.json"


def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def generate_id(expenses):
    return max((expense["id"] for expense in expenses), default=0) + 1


def add_expense(expenses):
    print("\n--- Add Expense ---")

    title = input("Expense name: ").strip()

    if not title:
        print("Expense name cannot be empty.")
        return

    while True:
        try:
            amount = float(input("Amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            break
        except ValueError:
            print("Please enter a valid amount.")

    category = input("Category: ").strip().title() or "Other"

    expense = {
        "id": generate_id(expenses),
        "title": title,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


def view_expenses(expenses):
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print(
            f"\nID: {expense['id']}"
            f"\nName: {expense['title']}"
            f"\nAmount: ${expense['amount']:.2f}"
            f"\nCategory: {expense['category']}"
            f"\nDate: {expense['date']}"
            "\n-------------------------"
        )


def calculate_total(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print("\n--- Total Spending ---")
    print(f"Total spent: ${total:.2f}")


def view_by_category(expenses):
    print("\n--- Expenses by Category ---")

    if not expenses:
        print("No expenses found.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        categories[category] = categories.get(category, 0) + expense["amount"]

    for category, amount in categories.items():
        print(f"{category}: ${amount:.2f}")


def search_expenses(expenses):
    print("\n--- Search Expenses ---")

    keyword = input("Search: ").strip().lower()

    results = [
        expense
        for expense in expenses
        if keyword in expense["title"].lower()
        or keyword in expense["category"].lower()
    ]

    if not results:
        print("No matching expenses found.")
        return

    for expense in results:
        print(
            f"{expense['id']} | "
            f"{expense['title']} | "
            f"${expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['date']}"
        )


def update_expense(expenses):
    print("\n--- Update Expense ---")

    try:
        expense_id = int(input("Enter expense ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    expense = next(
        (expense for expense in expenses if expense["id"] == expense_id),
        None
    )

    if not expense:
        print("Expense not found.")
        return

    new_title = input(
        f"New name [{expense['title']}]: "
    ).strip()

    if new_title:
        expense["title"] = new_title

    new_amount = input(
        f"New amount [{expense['amount']}]: "
    ).strip()

    if new_amount:
        try:
            new_amount = float(new_amount)

            if new_amount <= 0:
                print("Amount must be greater than zero.")
                return

            expense["amount"] = new_amount

        except ValueError:
            print("Invalid amount.")
            return

    new_category = input(
        f"New category [{expense['category']}]: "
    ).strip()

    if new_category:
        expense["category"] = new_category.title()

    save_expenses(expenses)

    print("Expense updated successfully!")


def delete_expense(expenses):
    print("\n--- Delete Expense ---")

    try:
        expense_id = int(input("Enter expense ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    expense = next(
        (expense for expense in expenses if expense["id"] == expense_id),
        None
    )

    if not expense:
        print("Expense not found.")
        return

    confirmation = input(
        f"Delete '{expense['title']}'? (y/n): "
    ).lower()

    if confirmation == "y":
        expenses.remove(expense)
        save_expenses(expenses)
        print("Expense deleted successfully!")
    else:
        print("Deletion cancelled.")


def monthly_report(expenses):
    print("\n--- Monthly Report ---")

    current_month = datetime.now().strftime("%Y-%m")

    monthly_expenses = [
        expense
        for expense in expenses
        if expense["date"].startswith(current_month)
    ]

    if not monthly_expenses:
        print("No expenses this month.")
        return

    total = sum(expense["amount"] for expense in monthly_expenses)

    print(f"Month: {current_month}")
    print(f"Expenses: {len(monthly_expenses)}")
    print(f"Total: ${total:.2f}")

    categories = {}

    for expense in monthly_expenses:
        category = expense["category"]
        categories[category] = categories.get(category, 0) + expense["amount"]

    print("\nCategory breakdown:")

    for category, amount in categories.items():
        percentage = (amount / total) * 100
        print(f"{category}: ${amount:.2f} ({percentage:.1f}%)")


def display_menu():
    print("""
╔════════════════════════════════╗
║          PYTRACK               ║
║    Personal Expense Tracker    ║
╠════════════════════════════════╣
║ 1. Add expense                 ║
║ 2. View expenses               ║
║ 3. View total spending         ║
║ 4. View by category            ║
║ 5. Search expenses             ║
║ 6. Update expense              ║
║ 7. Delete expense              ║
║ 8. Monthly report              ║
║ 9. Exit                        ║
╚════════════════════════════════╝
""")


def main():
    expenses = load_expenses()

    print("Welcome to PyTrack!")

    while True:
        display_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            calculate_total(expenses)

        elif choice == "4":
            view_by_category(expenses)

        elif choice == "5":
            search_expenses(expenses)

        elif choice == "6":
            update_expense(expenses)

        elif choice == "7":
            delete_expense(expenses)

        elif choice == "8":
            monthly_report(expenses)

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()