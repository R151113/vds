##program for linear convolution
len1=input("enter length of the first discrete signal:-")
len2=input("enter length of the second discrete signal:-")
x=[] 
y=[] 

for i in range (0,len1,1):
	a=input("enter the value:-")
	x.append(a)
for i in range (len2,0,-1):
	a=input("enter the number:-")
	y.append(a)
print y
z=[]
import numpy as np
z=np.ones(len1+len2-1)
for n in range (0,len1+len2-1):
   for k in range (0,len1):
      if ((n-k)>=0 and (n-k)<len2):
	   z[n]=z[n]+x[k]*y[n-k]

g=(z-np.ones(len1+len2-1))
print "after completion of linear convolution ,the output is:"
print "            "  ,g

