expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = input("Enter amount: ")

        expenses.append([item, amount])
        print("Expense added successfully!")

    elif choice == "2":
        print("\nExpenses:")
        for expense in expenses:
            print("Item:", expense[0], "| Amount:", expense[1])

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")