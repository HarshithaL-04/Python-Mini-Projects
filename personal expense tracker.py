#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Personal Expense Tracker

# Function to analyze expenses
def analyze_expenses(expenses):
    total = sum(expenses.values())  # Calculate total expense

    print("\n--- Expense Summary ---")
    print("Total Expense:", total)

    # Find category-wise expenses
    highest_category = ""
    highest_amount = 0

    for category, amount in expenses.items():
        print(f"{category}: {amount}")

        if amount > highest_amount:
            highest_amount = amount
            highest_category = category

    print("Highest Spending Category:", highest_category)


# Dictionary to store expenses
expenses = {}

n = int(input("Enter number of expense entries: "))

# Taking user input
for i in range(n):
    category = input(f"Enter category {i+1}: ")
    amount = int(input("Enter amount: "))

    # Add expense to dictionary
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

# Analyze the expense data
analyze_expenses(expenses)


# In[ ]:




