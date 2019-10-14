import numpy as np
from math import sqrt

data = [168,170,150,160,182,142,175]

#using numpy
variance = np.var(data)
print("Variance using numpy--->" ,variance)

#using step by step

mean = np.mean(data)
#print(mean)

l = []
for i in data:
    variance1 = (i-mean)**2
    l.append(variance1)


#print(l)

n=0
for i in l:
    n = n+i
v = n/len(data)
print("variance using mathematics-->" , v)

#standard deviation
print("Standard deviation(square root of variance)-->",np.std(data))

print("Standard deviation-->",sqrt(v))
