# -*- coding: utf-8 -*-
# Objective:Actual function is y=x**2, primary linear fit by OLS
# Author: 张子昂 Date: 20230309 Student Number: 202004060320

import numpy as np
import matplotlib.pyplot as plt
import random

sample_size1 = 100  # sample size used for linear fit
sample_size2 = 1000  # sample size used for error analysis
sum_x = 0  # sum of x of 100 points
sum_y = 0  # sum of y of 100 points
sum_xy = 0  # sum of x*y of 100 points
sum_x2 = 0  # sum of x^2 of 100 points

x_space = []
# create a list x_space storing 1100 random numbers as x values of these random points
for i in range(1100):
    a = random.random() * 100
    x_space.append(a)
# take the first 100 different random numbers from the x_space list
# and place them in list x1 and the rest 1000 in list x2
x1 = x_space[0:100]
x2 = x_space[100:]

y_space = []
# create a list y_space storing 1100 random numbers as y values at these random points
for i in range(1100):
    a = random.random() * 100
    y_space.append(a)
# take the first 100 different random numbers from the y_space list
# and place them in list y1 and the rest 1000 in list y2
y1 = y_space[0:100]
y2 = y_space[100:]

for i in range(100):
    # solve the primary fit function for a,b and output the function
    sum_x += x1[i]
    sum_y += y1[i]
    sum_xy += x1[i] * y1[i]
    sum_x2 += x1[i] * x1[i]
average_x = sum_x / sample_size1
average_y = sum_y / sample_size1
b = (sum_xy - sample_size1 * average_x * average_y) / (sum_x2 - sample_size1 * average_x * average_x)
a = average_y - b * average_x
print("y = {0}*x + ({1})".format(b, a))

sum_c2 = 0
for i in range(1000):
    y = b * x2[i] + a
    sum_c2 += (y - y2[i]) * (y - y2[i])
error = (sum_c2 / 1000) ** 0.5
print(error)
# use the fitting function to find the y value and perform a root-mean-square error analysis with the actual point
# and output the error value

X = np.linspace(0, 100, 1000)
Y = b * X + a
plt.plot(X, Y)
plt.title("y = {0}*x + ({1})".format(b, a))
plt.scatter(x2, y2)
plt.show()
# draw the fitting curves and discrete points