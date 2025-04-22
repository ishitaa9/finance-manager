# Expense Tracker Web Application

An **Expense Tracker** web application built using **Flask**. This app allows users to:
- Set and update a budget.
- Add expenses with categories (Food, Home, Work, Fun, Misc).
- View summaries of their expenses.
- See a pie chart representing expenditures by category.
- Get remaining budget and daily budget calculations based on the set budget and expenses.

## Features
- **Set and Update Budget**: Define a budget for tracking your expenses.
- **Add Expenses**: Add individual expenses with names, amounts, and categories.
- **Expense Summary**: View how much you've spent and how much is left.
- **Expenditure by Category**: View how your spending breaks down by category (Food, Home, Work, Fun, Misc).
- **Daily Budget Calculation**: Get a daily budget based on how many days are left in the current month.
- **Visualization**: A pie chart of expenditures across categories.

## Tech Stack
- **Backend**: Python with Flask
- **Frontend**: HTML, Jinja2 (templating engine)
- **Visualization**: Matplotlib (for pie chart)
- **Data Storage**: CSV files for storing expenses and budget
- **Deployment**: Flask application, can be hosted on platforms like Heroku or any other server.

## Installation

### 1. Clone this Repository:
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker 
   python3 -m venv venv
   source venv/bin/activate
   
