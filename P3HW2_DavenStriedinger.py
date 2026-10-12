# Daven Striedinger
# October 11, 2026
# P3HW2 - Salary
# A program to calculate regular pay, overtime pay, and gross pay for an employee.

"""
Pseudocode:
1. Prompt user to enter employee's name.
2. Prompt user to enter number of hours worked as a float.
3. Prompt user to enter employee's pay rate as a float.
4. Check if hours worked is greater than 40:
    - If True:
        - Overtime hours = hours worked - 40
        - Regular hours = 40
    - Else:
        - Overtime hours = 0
        - Regular hours = hours worked
5. Calculate pay components:
    - Overtime pay = overtime hours * (pay rate * 1.5)
    - Regular pay = regular hours * pay rate
    - Gross pay = regular pay + overtime pay
6. Display employee name.
7. Display headers: Hours Worked, Pay Rate, OverTime, OverTime Pay, RegHour Pay, Gross Pay.
8. Display calculated values formatted into aligned columns using f-strings.
"""

# Input employee details
emp_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Decision structure to calculate regular and overtime hours
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    reg_hours = 40.0
else:
    overtime_hours = 0.0
    reg_hours = hours_worked

# Calculate pay values
overtime_pay = overtime_hours * (pay_rate * 1.5)
reg_pay = reg_hours * pay_rate
gross_pay = reg_pay + overtime_pay

# Format dollar strings for RegHour Pay and Gross Pay to include $
reg_pay_str = f"${reg_pay:.2f}"
gross_pay_str = f"${gross_pay:.2f}"

# Display output matching the sample format exactly
print("----------------------------------------")
print(f"Employee name:   {emp_name}")
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<16}{'RegHour Pay':<16}{'Gross Pay':<12}")
print("--------------------------------------------------------------------------------------------------")
print(f"{hours_worked:<15.1f}{pay_rate:<12.1f}{overtime_hours:<12.1f}{overtime_pay:<16.2f}{reg_pay_str:<16}{gross_pay_str:<12}")