import pandas as pd
import numpy as np
data=pd.read_csv("new_deaths.csv")
n=len(data["Canada"])
days=120
y=data["Canada"][n-days:n]
x=np.arange(n-days,n)
from scipy.optimize import curve_fit
def func(x,a,b,c,d,e,f,g):
 return a*x*x*x*x*x*x+b*x*x*x*x*x+c*x*x*x*x+d*x*x*x+e*x*x+f*x+g
param=curve_fit(func,x,y)
[a,b,c,d,e,f,g]=param[0]
print(a,b,c,d,e,f,g)
print(data["date"][n-1]+'+7')
import matplotlib.pyplot as plt
print("Nov. 11 deaths",int(func(n-1+7,a,b,c,d,e,f,g)))
print("Nov. 18 deaths",int(func(n-1+14,a,b,c,d,e,f,g)))
print("Nov. 25 deaths",int(func(n-1+21,a,b,c,d,e,f,g)))
y=data["Canada"]
x=np.arange(len(y))
plt.plot(x,y)
x=np.arange(n-days,n)
plt.plot(x,func(x,a,b,c,d,e,f,g),'r')
x1=np.arange(n-days,n+25)
plt.plot(n-1+7,func(n-1+7,a,b,c,d,e,f,g),'ro')
plt.plot(n-1+14,func(n-1+14,a,b,c,d,e,f,g),'ro')
plt.plot(n-1+21,func(n-1+21,a,b,c,d,e,f,g),'ro')
plt.plot(x1,func(x1,a,b,c,d,e,f,g))
plt.show()
