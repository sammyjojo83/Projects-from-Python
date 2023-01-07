
# Name:             Samantha Merton
# Section:          Engineering 102 556
# Assignment:   PRETTY PLOTTING (Lab 12.16) 
# Date:              22 NOVEMBER, 2022

import numpy as np #impoting numpy to use under variable name np
import matplotlib.pyplot as plt #importing matplot as plt variable name
M = np.array([[1.01 ,0.09], [-0.09,1.01]]) #creating arrays
p = np.array([[0,1]])
v = p.transpose() #permutting array dimension
x = np.array([1]) #creating array
y = np.array([0])
for i in range(0,200): #setting up loop to repeat 200 times
    c = np.dot(M,v) #creating dot plot for 2-d array 
    x = np.append(x, c[0][0]) #appending new arrays
    y = np.append(y, c[1][0])
    v = c #
plt.plot(x, y, 'g--') #creating dash for outlining plot line
plt.xlabel('x-axis') #labeling x axis
plt.ylabel('y-axis') #Labeling y axis
plt.title('SPIRAL') #creating title for plot
plt.show() #command to show graph/plot
