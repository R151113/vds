import matplotlib.pyplot as plt 
import numpy as np
wp=float(input("enter wp="))
ws=float(input("enter the ws="))
x=float(input("enter del s value="))
y=float(input("enter del p="))
if(ws>wp):
 p=np.log(((1/x**2)-1)/((1/y**2)-1))
 q=np.log(wp/ws)
 n=0.5*(p/q)
 print("order of the filter is")
 a=((1/x**2)-1)
 b=(0.5/n)
 c=(a**b)
 wc=wp/c
 print("cut off frequency of the filter is")
 w=np.arange(0,100,10)
 h=1/((1+((w/wc)**(2*n)))**0.5)
plt.plot(w,h)
plt.show()
