expenses = []

def add_expense():
    description = input("Τι αγοράσατε; ")
    amount = float(input("Πόσο κόστισε; "))
    
    expense = {
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    print("Η καταχώρηση προστέθηκε!")

def show_expenses():
    print("\n--- Τα έξοδά μου ---")
    if not expenses:
        print("Δεν υπάρχουν καταχωρήσεις ακόμα.")
    else:
        for i, expense in enumerate(expenses):
            print(f"{i + 1}. {expense['description']}: {expense['amount']}€")
    print("--------------------\n")

def main():
    while True:
        print("1. Προσθήκη Εξόδου")
        print("2. Προβολή Εξόδων")
        print("3. Έξοδος")
        
        choice = input("Επίλεξε μια ενέργεια (1-3): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            print("Αντίο!")
            break
        else:
            print("Λάθος επιλογή, δοκίμασε ξανά.")

if __name__ == "__main__":
    main()
