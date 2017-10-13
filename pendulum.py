# pendulum.py made to interpret data from pendulum.txt; made by Frank Lee
# 10/10/17

import matplotlib.pyplot as plt 
import numpy as np

RawInputValues=np.loadtxt("pendulum.txt",delimiter=",")
InputValues=np.transpose(RawInputValues)
lencm=InputValues[0]
tenperiods=InputValues[1]
timeerror=0.1

lenmetre=0.01*lencm
periods=0.1*tenperiods

plt.figure(1)
plt.title("Period of pendulum vs length of string")
plt.xlabel("Length of string /m")
plt.ylabel("Period of pedulm /s")
plt.errorbar(lenmetre,periods,yerr=timeerror,fmt="ro")
plt.grid()

plt.figure(2)
plt.title("Period of pendulum squared vs length of string")
plt.xlabel("Length of string /m")
plt.ylabel("Period of pedulm /s^2")
plt.errorbar(lenmetre,periods**2,yerr=timeerror,fmt="ro")
m,b=np.polyfit(lenmetre, periods**2,1)
plt.plot(lenmetre,m*lenmetre+b)
print(m,b)
plt.grid()

plt.show()