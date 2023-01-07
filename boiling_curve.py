
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:                     Samantha Merton
#                        
#                         
# Section:          Engineering 102 (Zybook Boiling Point Curve )
# Date:               24, Sept 2022


from math import *

#user input for excess temperature
x = float(input("Enter the excess temperature:"))

#following are the calculations for each interval on the graph
#based off formula as seen on PDF
#each if and elif statment is a different interval
if x <= 1.2:
    print("Surface heat flux is not available")
elif x >= 1.3 and x <= 5:
    m = 1.444546222
    y = 1000 * ((x / 1.3)**(m))
    print(f'The surface heat flux is approximately {y:.0f} W/m^2')
elif x > 5 and x <= 30:
    m = 2.99555288
    y = 7000 * ((x / 5)**(m))
    print(f'The surface heat flux is approximately {y:.0f} W/m^2')
elif x > 30 and x <= 120:
    m = -2.953445297
    y = ((15*(10**5))) * ((x / 30)**(m))
    print(f'The surface heat flux is approximately {y:.0f} W/m^2')
elif x > 120 and x <= 1200:
    m = 1.77815125
    y = ((25)*(10**3))*((x/120)**(m))
    print(f'The surface heat flux is approximately {y:.0f} W/m^2')
elif x > 1200:
    print("Surface heat flux is not available") 

