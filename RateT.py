# RateT.py made to interpret RateT.txt; made my Frank Lee
# 7/10/17

import matplotlib.pyplot as plt
import numpy as np

RawInputValues=np.loadtxt("RateT.txt",delimiter=",")
InputValues=np.transpose(RawInputValues)
TempKelvin=InputValues[0]+273.15							#converting from Celsius to Kelvin
RateConstant=InputValues[1]

plt.figure(1)
plt.errorbar(1/TempKelvin, np.log(RateConstant), fmt="ro")	#Plotting ln(k) against (1/T) according to Arrhenius
m,b=np.polyfit(1/TempKelvin, np.log(RateConstant),1)		#Assuming a linear best fit
plt.plot(1/TempKelvin,m*(1/TempKelvin)+b,'-')
plt.title("Plotting 1/T vs ln(k)")
plt.xlabel("1/T \K^(-1)")
plt.ylabel("ln(k)")
print(m,b)													#Deducing y=mx+b
plt.show()

# Conclusion: E_a=16.6 kJ and A=100.2 s^(-1)