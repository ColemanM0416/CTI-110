#magan Coleman
#10/25/2026
#C!S-110
#Use loops to display info to user

#Ask user to enter a integer
#Determine if positive or negative
#If positive, display multiplication table
#If negative, tell user program cannot accept it. 
#Ask user ton run again?
#If yes, run again
#if no, end program

run_again = "yes"
while run_again != "no":


    num = int(input("Enter an integer:  "))

    if num >= 0:
        #dysplay multiplication in range from 1-12
        for item in range(1, 13):
            print(f"{num} * {item} = {num * item}")    

    else:
        print("This program does not handle negative numbers:")
    
    run_again = input("Would you like to run the program again? ")

#Loop has broken, user said no
print("Exiting program...")
