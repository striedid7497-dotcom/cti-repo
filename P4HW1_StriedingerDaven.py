# Daven Striedinger
# September 1, 2026
# P4HW1
# This program asks the user for a number of scores, validates them, drops the lowest score, and calculates the average grade.

# PSEUDOCODE:
# Get number of scores from user
# Create empty score list
# Loop for the number of scores requested
# Inside loop, ask for score and validate between 0 and 100 with a while loop
# Append valid score to list
# Find lowest score and remove it from a copy of the list
# Calculate average of remaining scores
# Determine letter grade using if-elif-else statements
# Print results

num_scores = int(input("How many scores do you want to enter? "))

scores = []

for i in range(num_scores):
    score = float(input(f"Enter score #{i+1}: "))
    
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i+1} again: "))
        
    scores.append(score)

# find lowest score
lowest = min(scores)

# create a modified list by copying and removing lowest
modified_list = []
for s in scores:
    modified_list.append(s)
modified_list.remove(lowest)

# calculate average manually or with sum/len
total = 0
for s in modified_list:
    total = total + s

average = total / len(modified_list)

# figure out letter grade
if average >= 90:
    grade = 'A'
else:
    if average >= 80:
        grade = 'B'
    else:
        if average >= 70:
            grade = 'C'
        else:
            if average >= 60:
                grade = 'D'
            else:
                grade = 'F'

print("\n-----------------Results-----------------")
print("Lowest Score  :", lowest)
print("Modified List :", modified_list)
print("Scores Average:", format(average, '.2f'))
print("Grade         :", grade)
print("-----------------------------------------")