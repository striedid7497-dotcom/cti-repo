# Daven Striedinger
# 2026-09-27
# P1HW2
# calculates travel budget

print("This program calculates and displays travel expenses\n")

budget = float(input("budget: "))
print()

dest = input("destination: ")
print()

gas = float(input("gas: "))
print()

hotel = float(input("hotel: "))
print()

food = float(input("food: "))
print()

expenses = gas + hotel + food
remaining = budget - expenses

print("------------Travel Expenses------------")
print(f"Location: {dest}")
print(f"Initial Budget: {budget:.0f}\n")
print(f"Fuel: {gas:.0f}")
print(f"Accomodation: {hotel:.0f}")
print(f"Food: {food:.0f}\n")
print(f"Remaining Balance: {remaining:.0f}")