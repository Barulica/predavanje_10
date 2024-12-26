
import json
import sys
from datetime import datetime

user = None
limit_budget = 100000

with open('data/test.json', 'r') as file:
    user = json.load(file)

maximum_budget = user ['budget'] + user ['loan']


if maximum_budget >= limit_budget or maximum_budget <= 0:
    print("Value is not correct")
    sys.exit()

formated_budget = f'{maximum_budget:.2f} {user["currency"]}'

print(f"Welcome back, {user['name']}! Your budget is {formated_budget}")

def clear_logs():
    with open('exercise/logs/expense.txt', 'w') as file:
        pass
    print("Logs cleared")


while True:
    print("\nMenu:")
    print("1. Enter an expense")
    print("2. Clear logs")
    print("3. Exit")

    choice = input("Choose an option: \n")

    if choice == '1':
        try:
            expense = int(input("Enter expense: \n"))

            if 0 < expense <= maximum_budget:

                maximum_budget -= expense
                budget_after_expense = maximum_budget

                print(f"{user['name']}, your budget is now {budget_after_expense}")


                with open('exercise/logs/expense.txt', 'a') as file:
                    message = (f"Amount of expense: {expense}, "f" "
                               f"User: {user['name']}, "
                               f"Budget:"f" {budget_after_expense} "
                               f"Datetime {datetime.now()}\n")
                    file.write(message)

            else:
                print("You don't have enough budget")

        except ValueError:
            print("Not valid input")

    elif choice == '2':
        clear_logs()

    elif choice == '3':
        print(f"Thank You, {user['name']}! Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
