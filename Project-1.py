import csv
import os
def add_expense(expenses):
    # Prompt the user for expense details
    
    date = input("Enter the date of expense (YYYY-DD-MM): " )
    category = input("Enter the category of expense(e.g., Food, travel) :" )
    amount = float(input("Enter the amoout spent: " ))
    description = input("Enter a brief description of the expense: ")
    # Create a dictionary for the expense
    
    expense = {
        'date': date,
        'category' : category,
        'amount' : amount,
        'description' : description,
        
    }
    
    #Add the expense to the list
    
    expenses.append(expense)
    print("Expense added Successfully!")
    
def view_expenses(expenses):
        # check if there are any expenses to display
        if not expenses:
            print("No expenses recorded.")
            return
        
        print("\nAll Expenses: ")
        for expense in expenses:
            # Validate that all required details are present
            
            if all(key in expense and expense[key] for key in ['date', 'category', 'amount', 'description']) :
                 print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")
            else:
                print("Incomplete expense entry found, skipping...")
            
def set_budget():
                budget = input("Enter your monthly budget : ")
                try:
                    budget = float(budget) 
                    return budget
                except ValueError:
                    print("Invalid budget. Please enter a numeric value.")
                return None
                
              
def track_budget(expenses, budget):
    """Calculate total expenses and compare with the budget."""
    total_expenses = sum(expense['amount'] for expense in expenses)
    
    print(f"Total Expenses: {total_expenses}, Budget: {budget}")
    if total_expenses > budget:
        print("You have exceeded your budget!")
    else:
        remaining_balance = budget - total_expenses
        print(f"You have {remaining_balance:.2f} left for the month.")
        
def save_expenses(expenses, filename = 'expenses.csv'):
    """Save all expense to a CSV file"""
    with open(filename, mode = 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)
        print("Expenses saved successfully!")
        
def load_expense(filename = 'expenses.csv'):
    """Load expenses from a CSV file"""
    expenses = []
    if os.path.exists(filename):
        with open(filename, mode = 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['amount'] = float(row['amount']) # Convert amount back to float
                expenses.append(row)
                
    return expenses     
            
def display_menu():
    """Display the interactive menu."""
    print("\nMenu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Track Budget")
    print("4. Save Expenses")
    print("5. Exit")
              
def main():
    """Main function to run the expense tracker program."""
    expenses = load_expense()  # Load expenses at the start
    budget = None

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_expense(expenses)
            
        elif choice == '2':
            view_expenses(expenses)
                      
        elif choice == '3':
            if budget is None:
                budget = set_budget()
            track_budget(expenses, budget)
             
       
        elif choice == '4':
            save_expenses(expenses)
        elif choice == '5':
            save_expenses(expenses)  # Save before exiting
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.") 
            

if __name__ == "__main__":
    main()
                
                    
                    
    
                   