# Magan Coleman
# 09/27/2026
# P2HW2
# Understanding Lists

# prompt grades


grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# Calculate required results

grades = [grade1, grade2, grade3, grade4, grade5, grade6]
Lowest = min(grades)
Highest = max(grades)
Sum = sum(grades)
Average = sum(grades) / len(grades)

# Display results
print("----------Results----------")
print(f'{"Lowest Grade: ":<20}{Lowest:>10.2f}')
print(f'{"Highest Grade: ":<20}{Highest:>10.2f}')
print(f'{"Sum of Grades: ":<20}{Sum:>10.2f}')
print(f'{"Average: ":<20}{Average:>10.2f}')