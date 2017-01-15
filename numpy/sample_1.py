import numpy as np

# Arranges the number 0 through 15 in a 5x3 grid (3 rows, 5 columns)
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape) # The shape of the array

print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))

b = np.array([6, 7, 8])
print(b)
print(type(b))
