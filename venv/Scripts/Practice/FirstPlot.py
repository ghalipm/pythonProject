import pandas as pd
from matplotlib import pyplot as plt
#
...
XList=[]
YList=[]
# interval (a,b), step length h
for x in range(-10,11,1):
    y=x**2+10
    print(x,y)
    XList.append(x)
    YList.append(y)
plt.plot(XList,YList)
...

x=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
y=[100,81,64,49,36,25,16,9,4,1,0,1,4,9,16,25,36,49,64,81,100]
plt.plot(x,y)
plt.title("First Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(['y line'])
plt.show()