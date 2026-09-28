# Magan Coleman
# 09/12/2026
# P1HW2

print("This program calculates and displays travel expenses")
print()

budget = float(input("Enter budget: "))
destination = (input("Enter your travel destination: "))
fuel = float(input("How much would you like to spend on gas? "))
accommodation = float(input("Approximately how much will you need for accommodations? "))
food = float(input("Last, how much do you need for food?  "))

expenses = fuel + accommodation + food
result = budget - expenses

print("--------Travel Expenses---------")
print()

print(f'{"Location: ":<20}{destination}')
print(f'{"Initial Budget: ":<20}${budget:>10.2f}')

print(f'{"Fuel: ":<20}${fuel:>10.2f}')
print(f'{"Accommodation: ":<20}${accommodation:>10.2f}')
print(f'{"Food: ":<20}${food:>10.2f}')
print("----------------------------------------")
print()
print(f'{"Remaining Balance: ":<20}${result:>10.2f}')
