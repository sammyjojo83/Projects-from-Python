
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
          
# Section:               Engineering 102

from math import *

ln = 2.718281828

sex = input("Enter your sex (M/F):")
ln = 2.718281828
if (sex == "M") or (sex == "m"):
    a = 0
if (sex == "F") or (sex == "f"):
    a = 0.879
    
age = int(input("Enter your age (years):")) #input for age
 
bmi = int(input("Enter your BMI:")) #input for bmi and storing number for end calculation
if bmi < 25:
    b = 0
elif bmi >= 25 or bmi <= 27.49:
    b = 0.699
elif bmi >= 27.5 or bmi <= 29.99:
    b = 1.97
elif bmi >= 30:
    b = 2.518

meds = input("Are you on medication for hypertension (Y/N)?") #input for hypertension meds and storing result
if meds == "N" or meds == "n":
    c = 0
if meds == "y" or meds == "Y":
    c = 1.222
    
roids = input("Are you on steroids (Y/N)?") #input for steroid meds and storing result
if roids == "N" or roids == "n":
    d = 0
if roids == "y" or roids == "Y":
    d = 2.191
    
cigs = input("Do you smoke cigarettes (Y/N)?") #input for cigs meds and storing result
if cigs == "N" or cigs == "n":
    past_nic = input("Did you use to smoke (Y/N)?") #previous nicotine usage
    if past_nic == "Y" or past_nic == "y":
        e = -0.218
    elif past_nic == "N" or past_nic == "n":
        e = 0
if cigs == "y" or cigs == "Y":
    e = 0.855

hx = input("Do you have a family history of diabetes (Y/N)?") #input for previous family hx
if hx == "N" or hx == "n":
    g = 0
if hx == "y" or hx == "Y":
    h = input("Was it your parents (Y/N)?")
    i = input("Was it your siblings (Y(/N)?")
    if (h == "y" or h == "Y") and (i == "y" or i == "Y"):
        g = 0.753
    if (h == "n" or h == "N") and (i == "y" or i == "Y"):
        g = 0.728
    if (h == "y" or h == "Y") and (i == "n" or i == "N"):
         g = 0.728
    
result = 6.322 + a - (0.063 * ((age))) - b - c - d - e - g

risk = (100) / (1 + ((ln)**(result))) 
risk = round(risk, 1)

print(f'Your risk of developing type-2 diabetes is {risk}%')

             


