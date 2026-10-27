#Magan Coleman
#10/27/2026
#P4HW2
#Edit and enhance an exisyting program

# Display info to user about salary


# enter user into

name = input("Enter employee's name or 'done' to terminate: ")

#Create acumulator vatiables 

overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0


while name != "done":
    # Add emp;oyee count = 1
    employee_count += 1
    #ask for employee info
    hours = float(input("How many hours did " +name+ " work? "))
    rate = float(input("What is " +name+"'s pay rate: "))


    # Use math

    if hours> 40:
        # Calculate overtime
        overtime_pay = hours - 40
        # Calculate overtime pay
        overtime_pay = (40 * rate) + (overtime_pay * rate * 1.5)
        # Calculate salary for regular hours
        regular_pay = 40 * rate
        # Calculate gross pay
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_pay = 0
        overttime_hrs = 0
        regular_pay = hours * rate
        gross_pay = regular_pay

    #Add accumulator variables
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay



    # Display results to user
    print("------------------------------------------------------")
    print("Employee Name:", name)
    print()
    print(f"{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<12}")
    print("------------------------------------------------------------------")
    print(f"{hours:<15}{rate:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<12}")
    print()

    name = input("Enter employee's name or 'done' to terminate: ")

#Gisplay final total
print()
print("Total number of employees entered:  ", employee_count)
print("Total amount paid for overtime:  $", format(overtimepay_total, ',.2f'))
print("Total amount paid for regular time:  $", format(regularpay_total, '.2f'))
print("Total amount paid in gross:  $", format(grosspay_total, '.2f'))

