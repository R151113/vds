from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
x=[1,1,1,1]

N=4
k=4
j=cm.sqrt(-1)
X=[]
w=np.linspace(-np.pi,np.pi,N)
for i in range(0,k):
    sum=0
    for n in range(0,len(x)):
       v=np.exp(-j*2*np.pi*i*n/N)
       sum=sum+(x[n]*v)
    X.append(sum)
        
plt.subplot(221)
plt.stem(np.abs(X))
plt.xlabel('freq(w/pi)')
plt.ylabel('magnitude')
plt.title('magnitude spectrum')
plt.grid()
plt.subplot(222)
plt.stem(angle(X)/np.pi)
plt.xlabel('freq(w/pi)')
plt.ylabel('phase angle in radian')
plt.title('phase spectrum')
plt.grid()
plt.show()
