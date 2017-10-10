# Flow.py made to interpret Flow.txt; made by Frank Lee
# 9/10/17

import matplotlib.pyplot as plt 
import numpy as np

RawInputValues=np.loadtxt("Flow.txt",delimiter=",")
InputValues=np.transpose(RawInputValues)
Diameter=InputValues[0]
FlowRate=InputValues[1]

plt.figure(1)
plt.title("Flow rate vs diameter")
plt.xlabel("Diameter")
plt.ylabel("Flow rate")
plt.errorbar(Diameter,FlowRate,fmt="ro")

plt.figure(2)
plt.title("Flow rate vs diameter log scale")
plt.xlabel("Diameter (log scale)")
plt.ylabel("flow rate")
plt.semilogx()
plt.errorbar(Diameter,FlowRate,fmt="ro")

plt.figure(3)
plt.title("Log scale flow rate vs diameter")
plt.xlabel("Diameter")
plt.ylabel("flow rate (log scale)")
plt.semilogy()
plt.errorbar(Diameter,FlowRate,fmt="ro")

plt.figure(4)
plt.title("Log scale flow rate vs log scale diameter")
plt.xlabel("Diameter (log scale)")
plt.ylabel("flow rate (log scale)")
plt.loglog()
plt.errorbar(Diameter,FlowRate,fmt="ro")

# looks like both axis with a log scale is the most clear. Straight line indicates a power law with its slope being the exponent

# Need to determine the slope for small and large diameters. Let the first 10 data points be 'small' diameters. 

smalldatax=[]
smalldatay=[]
for i in range(0,6):
	smalldatax.append(np.log10(Diameter[i]))
	smalldatay.append(np.log10(FlowRate[i]))

plt.figure(5)
plt.title("Log scale of flow rate vs log scale of small diameters")
plt.xlabel("Diameter (log scale)")
plt.ylabel("flow rate (log scale)")
plt.errorbar(smalldatax,smalldatay,fmt="ro")
m,b=np.polyfit(np.array(smalldatax), np.array(smalldatay),1)
print(m,b)

largedatax=[]
largedatay=[]
for i in range(32,40):
	largedatax.append(np.log10(Diameter[i]))
	largedatay.append(np.log10(FlowRate[i]))

m,b=np.polyfit(np.array(largedatax), np.array(largedatay),1)
print(m,b)

plt.show()