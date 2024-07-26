# Step 1: Print Statement

print("Welcome to Personal Finance Tracker!")
print("===================================")
print("This program helps you track your income, expenses, and savings.")
print("You can add income, add expenses, generate reports, and more.")
print("Let's get started!")

# Step 2: Variables

# Variables to store financial data
income = 0.0
expenses = 0.0
savings = 0.0
transactions = []

# Step 3: Data Types

# Data types:
# income, expenses, savings are floating-point numbers
# transactions is a list to store dictionaries for each transaction

# Step 4: Input and Output

# Basic interface example:
def main():
    print("Welcome to Personal Finance Tracker!")
    print("===================================")
    while True:
        print("\nOptions:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Generate Reports")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_income()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            generate_reports()
        elif choice == '4':
            print("Thank you for using Personal Finance Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

def add_income():
    global income
    amount = float(input("Enter income amount: "))
    income += amount
    transactions.append({'type': 'income', 'amount': amount})

def add_expense():
    global expenses
    amount = float(input("Enter expense amount: "))
    expenses += amount
    transactions.append({'type': 'expense', 'amount': amount})

def generate_reports():
    print("\n--- Financial Report ---")
    print(f"Income: ${income}")
    print(f"Expenses: ${expenses}")
    print(f"Savings: ${income - expenses}")

if __name__ == "__main__":
    main()

# Step 5: Functions

# Functions for adding income, expenses, and generating reports

def add_income(amount):
    global income
    income += amount
    transactions.append({'type': 'income', 'amount': amount})

def add_expense(amount):
    global expenses
    expenses += amount
    transactions.append({'type': 'expense', 'amount': amount})

def generate_reports():
    print("\n--- Financial Report ---")
    print(f"Income: ${income}")
    print(f"Expenses: ${expenses}")
    print(f"Savings: ${income - expenses}")

# Example usage:
add_income(1000.0)
add_expense(300.0)
generate_reports()

# Step 6: Conditional Statements 

# Example of using conditional statements in a main program loop

def main():
    print("Welcome to Personal Finance Tracker!")
    print("===================================")
    while True:
        print("\nOptions:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Generate Reports")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            amount = float(input("Enter income amount: "))
            add_income(amount)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            add_expense(amount)
        elif choice == '3':
            generate_reports()
        elif choice == '4':
            print("Thank you for using Personal Finance Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()

# Step 7: File Handling

# Example for file handling:
import json

def save_transactions():
    with open('transactions.json', 'w') as f:
        json.dump(transactions, f)

def load_transactions():
    global transactions
    try:
        with open('transactions.json', 'r') as f:
            transactions = json.load(f)
    except FileNotFoundError:
        transactions = []

# Call save_transactions() and load_transactions() appropriately in your program

# Step 8: Categories and reports

# Example of categorizing expenses

def add_expense(amount, category):
    global expenses
    expenses += amount
    transactions.append({'type': 'expense', 'amount': amount, 'category': category})

# Example usage:
add_expense(50.0, 'Groceries')
add_expense(100.0, 'Utilities')

# Function to generate a report by category
def generate_category_report(category):
    total_expense = 0.0
    for transaction in transactions:
        if transaction['type'] == 'expense' and transaction.get('category') == category:
            total_expense += transaction['amount']
    
    print(f"Total expenses in {category}: ${total_expense}")

# Example usage:
generate_category_report('Groceries')
generate_category_report('Utilities')

# Step 9: Data Visualization

# Example of data visualization (using matplotlib):
import matplotlib.pyplot as plt

def visualize_data():
    categories = {}
    for transaction in transactions:
        if transaction['type'] == 'expense':
            category = transaction.get('category', 'Uncategorized')
            if category in categories:
                categories[category] += transaction['amount']
            else:
                categories[category] = transaction['amount']

    plt.figure(figsize=(10, 6))
    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Expense Distribution')
    plt.axis('equal')
    plt.show()

# Call visualize_data() function where appropriate

# Step 10: Error Handling and Validation

# Example of error handling when adding income

def add_income(amount):
    global income
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid input. Please enter a valid number for amount.")
        return
    
    income += amount
    transactions.append({'type': 'income', 'amount': amount})

# Example usage:
add_income('abc')  # This will trigger the error handling
add_income(500.0)  # This will add income successfully

# Step 12: Conclusion

print("Thank you for using Personal Finance Tracker!")
