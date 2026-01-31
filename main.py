expenses = []

def add_expense():
    """
    Prompts the user for a description and amount,
    and adds the expense to the list.
    """
    description = input("What did you buy? ")
    # This line will crash if text is entered (Bug to be fixed later)
    amount = float(input("Enter amount: ")) 
    
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

def main():
    print(f"=== Budget Buddy v{VERSION} ===")
    
    while True:
        print("\n-------- MENU --------")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        print("----------------------")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
