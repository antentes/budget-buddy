expenses = []

def add_expense():
    """
    Prompts the user for a description and amount,
    and adds the expense to the list.
    """
    description = input("What did you buy? ")
    
    # Simple error handling for amount
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    expense = {
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    print("Expense added successfully!")

def show_expenses():
    """
    Displays all recorded expenses in a list format.
    """
    print("\n--- My Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
    else:
        for i, expense in enumerate(expenses):
            print(f"{i + 1}. {expense['description']}: {expense['amount']}€")
    print("-------------------\n")

def delete_expense():
    """
    Asks the user to select an expense ID and removes it.
    """
    show_expenses()
    if not expenses:
        return

    try:
        choice = int(input("Enter the number of the expense to delete: "))
        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            print(f"Deleted: {removed['description']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    print(f"=== Budget Buddy v{VERSION} ===")
    
    while True:
        print("\n-------- MENU --------")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")  
        print("4. Exit")
        print("----------------------")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            delete_expense() 
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
