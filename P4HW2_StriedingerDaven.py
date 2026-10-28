# Daven Striedinger
# September 1, 2026
# P4LAB2
# This program asks the user for an integer, checks if it is positive or zero 
# to display its multiplication table from 1 to 12 using a for loop, handles 
# negative integers with an error message, and uses a while loop to let the user 
# run the program again if desired.

# PSEUDOCODE:
# 1. Set run_program variable to "yes"
# 2. Start a while loop that runs as long as run_program equals "yes" (case-insensitive)
# 3. Ask user to enter an integer
# 4. If integer is greater than or equal to 0:
#    a. Use a for loop from 1 to 12
#    b. Multiply the user's integer by the loop counter
#    c. Print the multiplication equation and result
# 5. Else (if integer is less than 0):
#    a. Display a message stating negative numbers are not accepted / handled
# 6. Ask user if they would like to run the program again ("yes" or "no")
# 7. Update run_program variable with user's input
# 8. If user enters "no", break loop or end program with an exit message

run_program = "yes"

while run_program.lower() == "yes":
    # Input step: get an integer from the user
    user_num = int(input("Enter an integer: "))
    
    # Decision for positive vs. negative integer
    if user_num >= 0:
        # Multiplication table logic using a for loop (1 to 12)
        for i in range(1, 13):
            result = user_num * i
            print(f"{user_num} * {i} = {result}")
    else:
        # Negative number handling message
        print("This program does not handle negative numbers.")
        
    # Repeat/run-again logic
    print()
    run_program = input("Would you like to run the program again? ")
    print()

# Program exit condition
print("Exiting program...")