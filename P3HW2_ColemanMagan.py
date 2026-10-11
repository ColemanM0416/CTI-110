# Magan Coleman
# 10/08/2026
# P3HW2
# Display info to user about salary


# enter user into

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))

# Use math

if hours> 40:
    # Calculate overtime
    overtime_hrs = hours - 40
    # Calculate overtime pay
    overtime_pay = (40 * rate) + (overtime_hrs * rate * 1.5)
    # Calculate salary for regular hours
    reghrs = 40 * rate
    # Calculate gross pay
    gross_pay = reghrs + overtime_pay
else:
    overtime_pay = 0
    overttime_hrs = 0
    reghrs = hours * rate
    gross_pay = reghrs

# Display results to user
print("------------------------------------------------------")
print("Employee Name:", name)
print()
print(f"{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<12}")
print("------------------------------------------------------------------")
print(f"{hours:<15}{rate:<12}{overtime_pay:<15}{reghrs:<15}{gross_pay:<12}")