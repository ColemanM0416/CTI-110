# Magan Coleman
# 09/12/2026
# P1HW2

print("This program calculates and displays travel expenses")
print()

budget = int(input("Enter budget: "))
destination = (input("Enter your travel destination: "))
fuel = int(input("How much would you like to spend on gas? "))
accommodation = int(input("Approximately how much will you need for accommodations? "))
food = int(input("Last, how much do you need for food?  "))

expenses = fuel + accommodation + food
result = budget - expenses

print("--------Travel Expenses---------")
print()

print("Location:  ", destination)
print("Initial Budget:  ", budget)

print("Fuel:  ", fuel)
print("Accommodation:  ", accommodation)
print("Food:  ", food)

print("Remaining Balance:  ", result)
