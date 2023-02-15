import numpy as np 
size=int(1e4)

floats = np.random.uniform(size=size)
sum1= floats.sum()

np.random.shuffle(floats)

sum2= floats.sum()

print(sum1 == sum2)
print(f"{sum1}\n{sum2}")
