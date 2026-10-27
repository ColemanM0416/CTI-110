# Magan Coleman
# 10/25/2026
# P4HW1
# Edit and enhance existing program

# Ask user to input the number of scores they would like to enter.
# Create a loop to collect the number of scores the user wants to enter.
# If the score is valid, it should be between 0 and 100.
# If it is not, notify the user and ask for a valid score.

scores = []

num_scores = int(input("How many scores do you want to enter?  "))
print()

if num_scores <= 0:
    print("Number of scores must be greater than 0.")
else:
    for item in range(1, num_scores + 1):
        score = int(input(f"Enter score #{item}: "))
        while score < 0 or score > 100:
            print()
            print("INVALID Score entered!")
            print("Score should be between 0 and 100")
            score = int(input(f"Enter score #{item} again: "))
        scores.append(score)

    lowest_score = min(scores)
    modified_list = scores.copy()
    modified_list.remove(lowest_score)

    if modified_list:
        average = sum(modified_list) / len(modified_list)
        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"
    else:
        average = 0
        grade = "N/A"

 #create display table  
    print()
    print("--------------Results-----------------")
    print(f"{'Lowest Score':<20}: {lowest_score:.1f}")
    print(f"{'Modified List':<20}: [{', '.join(f'{score:^6.1f}' for score in modified_list)}]")
    print(f"{'Scores Average:':<20}: {average:.2f}")
    print(f"{'Grade:':<20}: {grade}")