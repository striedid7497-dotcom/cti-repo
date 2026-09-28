# Daven Striedinger
# 2026-09-27
# P2HW2
# calculates module grades

"""
Pseudocode:
1. Prompt user to enter float grades for modules 1 through 6 individually
2. Store all 6 grades into a list named module_grades_list
3. Determine lowest grade using min()
4. Determine highest grade using max()
5. Calculate sum of grades using sum()
6. Calculate average by dividing sum by list length
7. Print formatted results table matching required column widths and decimal places
"""

m1 = float(input("Enter grade for Module 1: "))
m2 = float(input("Enter grade for Module 2: "))
m3 = float(input("Enter grade for Module 3: "))
m4 = float(input("Enter grade for Module 4: "))
m5 = float(input("Enter grade for Module 5: "))
m6 = float(input("Enter grade for Module 6: "))

module_grades_list = [m1, m2, m3, m4, m5, m6]

lowest_grade = min(module_grades_list)
highest_grade = max(module_grades_list)
sum_of_grades = sum(module_grades_list)
average_grade = sum_of_grades / len(module_grades_list)

print()
print("------------Results------------")
print(f"{'Lowest Grade:':<16} {lowest_grade:.1f}")
print(f"{'Highest Grade:':<16} {highest_grade:.1f}")
print(f"{'Sum of Grades:':<16} {sum_of_grades:.1f}")
print(f"{'Average:':<16} {average_grade:.2f}")
print("----------------------------------------")