# 2000, 500, 100, 50, 20, 10, 5, 1

currencies = [2000, 500, 200, 100, 50, 20, 10]
total_amount = int(input("Enter amount: "))

get_currencies = {}

remaining_amount = total_amount

if total_amount < 10:
    print("Please enter more than 10 ruppes.")
else:
    for currency in currencies:
        get_currency = remaining_amount // currency  # Calculate the count of the current currency
        remaining_amount -= get_currency * currency  # Update the remaining amount
        get_currencies[currency] = get_currency     # Store the count in the dictionary

    print(get_currencies)