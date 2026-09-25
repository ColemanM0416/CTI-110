#Magan Coleman
#09?17/2026
#P2LAB1
#Mathmatical code for calculating circumfrence, diameter, and area.

import math


# Det Radius from user
radius = float(input("What is the radius of the circle?  "))
print()

#calculate rdiameter
diameter = 2 * radius
print()

#Display diameter with 1 decimal poiny
print(f"The diameter of the circle is {diameter:.1f}\n")

#Calculate circumfrence
circumfrence = 2 * math.pi * radius

#Display circumference with 2 decimal places
print(f"The circumfrence of the circle is {circumfrence:.2f}\n")

#calculate the area
area = math.pi * radius**2

#Display the area with 3 decimal places
print(f"The area of the circle is {area:.3f}\n")
