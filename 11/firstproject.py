
import json
import sys

user = None
limit_budget = 100000

with open('data/test.json', 'r') as file:
    user = json.load(file)

maximum_budget = user ['budget'] + user ['loan']


if maximum_budget >= limit_budget or maximum_budget <= 0:
    print("Value is not correct")
    sys.exit()

print(f"Welcome back, {user['name']}! Your budget is {maximum_budget}")

expense = 0

while expense <= 0 or expense >= maximum_budget:
    expense = int(input("Enter expense: \n"))

budget_after_expense = maximum_budget - expense
print(f"{user['name']}, your budget is now {budget_after_expense}")