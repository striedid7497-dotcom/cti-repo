cars = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = cars.keys()
print(keys)

vehicle = input("\nenter a vehicle to see it's mpg: ")
mpg = cars[vehicle]
print(f"\n{vehicle} gets {mpg} mpg.\n")

miles = float(input(f"how many miles will you drive {vehicle}? "))
gallons = miles / mpg
print(f"\n{gallons:.2f} gallon(s) of gas are needed to drive {vehicle} {miles} miles.")