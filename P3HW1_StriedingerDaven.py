# Daven Striedinger
# October 11, 2026
# P3HW1 - Debugging
# Correcting bugs in a program that calculates list statistics and determines a letter grade.

# Pseudocode:
# 1. Prompt user to enter grades for Module 1 through Module 6 as floating-point numbers.
# 2. Store all six grades in a list.
# 3. Calculate lowest grade, highest grade, sum of grades, and average grade.
# 4. Display the results formatted neatly.
# 5. Determine and output the letter grade based on the numeric average:
#    - 90 or higher = A
#    - 80 to 89.99 = B
#    - 70 to 79.99 = C
#    - 60 to 69.99 = D
#    - Below 60 = F

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total_sum = sum(grades)
avg = total_sum / len(grades)

# Display results formatted to match sample output
print('\n------------Results------------')
print(f'Lowest Grade:     {low:.1f}')
print(f'Highest Grade:    {high:.1f}')
print(f'Sum of Grades:    {total_sum:.1f}')
print(f'Average:          {avg:.2f}')
print('----------------------------------------')

# Determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')