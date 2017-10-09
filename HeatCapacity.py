# HeatCapacity.py made to interpret HeatCapacity.txt; made by Frank Lee
# 7/10/17

import matplotlib.pyplot as plt 
import numpy as np

RawInputValues=np.loadtxt("HeatCapacity.txt",delimiter=",")
InputValues=np.transpose(RawInputValues)
TempValues=InputValues[0]
HeatCap=InputValues[1]

# sorting alg. to determine lowest value in array. Slow O(n) alg. 

def findmin(arry,len,indexstep):
	min=arry[0]
	for i in range(1,len):
		if arry[i]<min:
			min=arry[i]
			minind=i
	print("The min value is: ",min," at index: ",minind,".\n")
	print("Therefore, the k-value is: ",minind*indexstep," with variance: ",min,".")

# We know that C~(T+kT^3) for some constant k.

def findkvalue():
	vararray=[]
	k=0
	i=0
	while (k<=0.05):
		length=len(InputValues[0])
		constantarray=[]
		for i in range(0,length):
			approx=TempValues[i]+k*(TempValues[i])**3
			actual=HeatCap[i]
			constant=actual/approx
			constantarray.append(constant)
		summ=0
		for data in constantarray:
			summ=summ+data
		mean=summ/length
		summm=0
		for moredata in constantarray:
			summm=summm+(moredata-mean)**2
		var=summm/length
		vararray.append(var)
		k=k+0.001
	print(vararray)
	findmin(vararray,len(vararray),0.001)

# Looks like k=0.005. Now we need the constant

def findnewconst():
	length=len(InputValues[0])
	conss=[]
	for i in range(0,length):
		right=TempValues[i]+0.005*(TempValues[i])**3
		left=HeatCap[i]
		cc=left/right
		conss.append(cc)
	print(conss)
	av=0
	for data in conss:
		av=av+data
	av=av/length
	print("The new constant is therefore:",av,".")

# Turns out, our new constant is 2. Therefore, C_v=2(T+0.005T^3) or A=2, B=0.01 where C_v=AT+BT^3

plt.figure(1)
plt.errorbar(TempValues,HeatCap,fmt="ro")
x_values=TempValues
y_values=2*TempValues+0.01*(TempValues)**3
plt.plot(x_values,y_values)
plt.show()