from flask import Flask, render_template, request, redirect, url_for
from expense import Expense
import datetime
import calendar

app = Flask(__name__)

# Simulating your expense file and budget (for simplicity)
expense_file_path = "expenses.csv"
budget = 2000

@app.route('/')
def index():
    return redirect(url_for('add_expense'))

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        # process the form data and save the expense
        expense_name = request.form['name']
        expense_amount = request.form['amount']
        expense_category = request.form['category']
        
        expense = Expense(name=expense_name, amount=expense_amount, category=expense_category)
        save_expense_to_file(expense, 'expenses.csv')  # Saving to file

        return redirect(url_for('summary'))  # After adding, redirect to summary page
    return render_template('add_expense.html')


@app.route('/summary')
def summary():
    expense_file_path = "expenses.csv"
    
    # Read expenses from the CSV file
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        
        # Skip the header row (first line)
        header = lines[0].strip().split(", ")
        
        # Process the remaining lines
        for line in lines[1:]:
            stripped_line = line.strip()  # Remove extra whitespace
            
            # Skip empty lines
            if not stripped_line:
                continue

            # Split the line into expense_name, expense_amount, and expense_category
            parts = stripped_line.split(", ")
            
            # Skip lines that don't have exactly 3 values
            if len(parts) != 3:
                print(f"Skipping invalid row: {line.strip()}")
                continue
            
            expense_name, expense_amount, expense_category = parts
            
            try:
                expense = {
                    'name': expense_name,
                    'amount': float(expense_amount),  # Ensure it's a float
                    'category': expense_category
                }
                expenses.append(expense)
            except ValueError:
                # Handle any invalid rows (like malformed data that can't be converted to float)
                print(f"Skipping invalid row (non-numeric value): {line.strip()}")
    
    # Calculate total amount by category
    amount_by_category = {}
    for expense in expenses:
        category = expense['category']
        if category in amount_by_category:
            amount_by_category[category] += expense['amount']
        else:
            amount_by_category[category] = expense['amount']
    
    # Total amount spent and budget remaining
    total_spent = sum(expense['amount'] for expense in expenses)
    remaining_budget = 2000 - total_spent
    daily_budget = remaining_budget / 10  # Assuming 10 days left in the month

    return render_template('summary.html',
                           amount_by_category=amount_by_category,
                           total_spent=total_spent,
                           remaining_budget=remaining_budget,
                           daily_budget=daily_budget,
                           expenses=expenses)


def save_expense_to_file(expense: Expense, expense_file_path):
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")

def read_expenses_from_file(expense_file_path):
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = stripped_line.split(", ")
            line_expense = Expense(
                name=expense_name, 
                amount=float(expense_amount), 
                category=expense_category
            )
            expenses.append(line_expense)
    return expenses

def summarize_expenses_by_category(expenses):
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    return amount_by_category

if __name__ == "__main__":
    app.run(debug=True)
