# example_plot.py from PHYS13AH; modified by Frank Lee
# 7/10/17

import matplotlib.pyplot as plt
import numpy as np
from math import * #turns out numpy and math conflict with each other 


# Actual plot e^(-x)cos(x) where x is in [0,20]
x_values = np.linspace(0,20,100)  						# produce 100 equally spaced points between 0 and 20 (want continuity)
y_values = (np.exp(-0.1*x_values))*(np.cos(x_values))	# plotting e^(-x)cos(x), would use math lib. but conflicting
plt.figure(1) 	
plt.title("Plot of y=e^(-0.1x)cos(x)")					# First plot is figure1
plt.plot(x_values, y_values) 							# Plot theory data, line connects points


# Plot of the data values given by data.txt
ExperimentInput = np.loadtxt("data.txt", delimiter=",")	# load input data from file, comma separated
print(ExperimentInput,"\n")								# checking if data array is functioning 
Experiment = np.transpose(ExperimentInput)				# transpose so x, y, y-error are separate row vectors
print(Experiment)										# checking if array is functioning 
x_data = Experiment[0]									# for clarity, explicitly name vectors
y_data = Experiment[1]
y_error = Experiment[2]
plt.figure(2)											# next plot is figure2
plt.errorbar(x_data, y_data, yerr=y_error, fmt='kx')  	# scatter plot with error bars, 'kx'=plot as black x
#plot(x_data, y_data,'k.')  							# plots without error bars, 'k.' plots as black points
plt.title("Actual plot of the data (should look like y~e^(-0.1x)cos(x))")


# example of combining theory and data plot
plt.figure(3)
plt.plot(x_values, y_values) 							# plot the theoretical function
plt.errorbar(x_data, y_data, yerr=y_error, fmt='ro')  	# on top, also plot experiment, 'ro'=plot as red o
plt.xlabel("x values")									# Always label your plots!
plt.ylabel("y values")
plt.title("Plot of the data values against the curve e^(-0.1x)cos(x)")
#plt.semilogx()											# now plot x on log axis. (Not needed for my customised data)
# xlim([0.5, 25])										# manual definition of x axis limits [xmin, xmax]
# ylim([-20, 450])										# manual definition of y axis limits [ymin, ymax]
plt.show()												# display figures(), always do last

# These are the commands to make a log plot in y or both
# semilogy()
# loglog()