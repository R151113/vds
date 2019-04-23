#27-feb-2018/dtft
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
x=[1,2,3,4,5,6,7,8,9,10]
N=100
j=cm.sqrt(-1)
X=[]
w=np.linspace(-np.pi,np.pi,N)
for i in range(0,N):
        sum=0
        for n in range(0,len(x)):
            sum=sum+(x[n]*np.exp(-n*w[i]*j))
        X.append(sum)
plt.subplot(221)
plt.plot(w,np.abs(X))
plt.xlabel('freq(w/pi)')
plt.ylabel('magnitude')
plt.title('magnitude spectrum')
plt.grid()
plt.subplot(222)
plt.plot(w,angle(X)/np.pi)
plt.xlabel('freq(w/pi)')
plt.ylabel('phase angle in radian')
plt.title('phase spectrum')
plt.grid()
plt.subplot(223)
plt.plot(w,real(X))
plt.xlabel('freq(w/pi)')
plt.ylabel('real part')
plt.title('real values of x')
plt.grid()
plt.subplot(224)
plt.plot(w,imag(X))
plt.xlabel('freq(w/pi)')
plt.ylabel('imaginary part')
plt.title('imaginary values of x')
plt.grid()
plt.show()
    
