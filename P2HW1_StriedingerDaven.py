# Daven Striedinger
# 2026-09-27
# P2HW1
# formats travel budget

print("This program calculates and displays travel expenses\n")

budget = float(input("budget: "))
dest = input("destination: ")
gas = float(input("gas: "))
hotel = float(input("hotel: "))
food = float(input("food: "))

expenses = gas + hotel + food
remaining = budget - expenses

print()
print("------------Travel Expenses------------")
print(f"{'Location:':<20} {dest}")
print(f"{'Initial Budget:':<20} ${budget:.2f}")
print(f"{'Fuel:':<20} ${gas:.2f}")
print(f"{'Accomodation:':<20} ${hotel:.2f}")
print(f"{'Food:':<20} ${food:.2f}")
print("---------------------------------------")
print(f"{'Remaining Balance:':<20} ${remaining:.2f}")