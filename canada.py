import pandas as pd
import numpy as np
data=pd.read_csv("canada.csv")
n=len(data["canada"])
y=data["canada"][n-120:n-1]
x=np.arange(n-120,n-1)
from scipy.optimize import curve_fit
def func(x,a,b,c,d,e,f,g):
 return a*x*x*x*x*x*x+b*x*x*x*x*x+c*x*x*x*x+d*x*x*x+e*x*x+f*x+g
param=curve_fit(func,x,y)
[a,b,c,d,e,f,g]=param[0]
print(a,b,c,d,e,f,g)
import matplotlib.pyplot as plt
print("Nov. 7 deaths",int(func(235+7,a,b,c,d,e,f,g)))
print("Nov. 14 deaths",int(func(235+14,a,b,c,d,e,f,g)))
print("Nov. 21 deaths",int(func(235+21,a,b,c,d,e,f,g)))
y=data["canada"]
x=np.arange(len(y))
plt.plot(x,y)

x=np.arange(n-120,n-1)
plt.plot(x,func(x,a,b,c,d,e,f,g),'r')
x1=np.arange(n-120,n+25)
plt.plot(236+7,func(236+7,a,b,c,d,e,f,g),'ro')
plt.plot(236+14,func(236+14,a,b,c,d,e,f,g),'ro')
plt.plot(236+21,func(236+21,a,b,c,d,e,f,g),'ro')
plt.plot(x1,func(x1,a,b,c,d,e,f,g))
plt.show()
