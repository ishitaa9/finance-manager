from expense import Expense
import datetime
import calendar

def main():
    print(f"🎯 Running Expense Tracker")
    expense_file_path = "expenses.csv"
    budget = 2000

    # user inputs expense
    expense = get_user_expense()
    # print(expense)

    # write expense to a file
    save_expense_to_file(expense, expense_file_path)

    # read file and summarize expenses
    summarize_expense(expense_file_path, budget)
    


def get_user_expense():
    print(f"🎯 getting expense")
    expense_name = (input("Enter expense name: "))
    expense_amount = float(input("Enter expense amount: "))
    # print(f"You've entered : {expense_name}, {expense_amount}")
    expense_categories = [
        "🍔 Food", 
        "🏡 Home", 
        "💼 Work", 
        "🎊 Fun", 
        "✨ Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, amount=expense_amount, category=selected_category)
            return new_expense
        else:
            print("Invalid category, please try again.")



def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"🎯 Saving expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category} \n")
    

def summarize_expense(expense_file_path, budget):
    print(f"🎯 summarizing expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip() #removes white spaces/lines
            expense_name, expense_amount, expense_category = stripped_line.split(",")
            # print(expense_name, expense_amount, expense_category)
            line_expense = Expense(
                name=expense_name, 
                amount=float(expense_amount), 
                category=expense_category
            )
            # print(line_expense)
            expenses.append(line_expense)
    # print(expenses)

    #dictionary; key is category, and value of key is the expense total of that category
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else: 
            amount_by_category[key] = expense.amount

    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"   {key}: €{amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"💸 You've spent €{total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"✅ Budget Remaining €{remaining_budget:.2f}")

    
    now = datetime.datetime.now() #get current date
    days_in_month = calendar.monthrange(now.year, now.month)[1]     #get no. of days in current month
    remaining_days = days_in_month - now.day #calc. the remaining no. of days in the current month
    daily_budget = remaining_budget/remaining_days
    print(green(f"👉 Budget Per Day: €{daily_budget:.2f}"))

def green(text):
    return f"\033[92m{text}\033[0m"

if __name__ == "__main__":
    main()