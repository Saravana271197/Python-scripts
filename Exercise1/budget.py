
cash_in_hand = int(input("Cash you have:"))
weekly_grocery_expense = int(input("Expenses for groceries:"))
weekly_personal_expense = int(input("Expenses for personal use:"))
Total_weeks = int(input("No of weeks:"))
def budget_calculator():
    Total_expenditure_per_semester = Total_weeks * (weekly_grocery_expense + weekly_personal_expense)
    print("My total expenditure this semester is:", Total_expenditure_per_semester)
    Total_cash_left = cash_in_hand - Total_expenditure_per_semester
    print("Cash left after my expenses in this semester", Total_cash_left)

budget_calculator()
