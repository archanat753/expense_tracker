import csv
from datetime import datetime

FILENAME = "expenses.csv"

# Ensure file exists with header
def init_file():
    try:
        with open(FILENAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])
    except FileExistsError:
        pass

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Shopping, etc): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note (optional): ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("✅ Expense added successfully!")

def view_expenses():
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        print("\n📒 Your Expenses:")
        print("Date       | Category | Amount | Note")
        print("-" * 40)
        for row in reader:
            print(" | ".join(row))

def total_expenses():
    total = 0
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[2])
    print(f"\n💰 Total Expenses: {total}")

def main():
    init_file()
    while True:
        print("\n📌 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()