import numpy as np

a = np.array([[1, 2], [3, 4]], dtype=complex)
print(a)

# Initialize an array of zeros
b = np.zeros((3, 4))
print(b)

# Initialize an array of all ones (2 sets of a 3x4 array)
c = np.ones((2, 3, 4), dtype=np.int16)
print(c)

d = np.empty((2, 3))
print(d)

# Reshaping a generated array into multiple sets
e = np.arange(24).reshape(2, 3, 4)
print(e)

# Printing the rows out
for row in e:
    for embedded_row in row:
        print embedded_row
        
print("\nBasic Operations\n")

# Basic operations
f = np.array([20, 30, 40, 50])
g = np.arange(4)
print(f - g)
print(g ** 2)
print(a < 35)
g *= 3
print(g)

h = np.random.random((2, 3))
print(h)
print(h.sum())
print(h.min())
print(h.max())

i = np.arange(3)
print(np.exp(i))

j = np.arange(10) ** 2
print(j)
