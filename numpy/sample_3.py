# Broadcasting examples
import numpy as np

# Adds the elements regardless of the size of the arrays
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([1, 0, 1])
print(x + y)

# Other operations work as well (multiplication, for example)
print(x * y)

# Other applications of broadcasting

# Compute outer product of vectors
a = np.array([1, 2, 3]) # Shape of (3, 1)
b = np.array([4, 5]) # Shape of (2, 1)

print(np.reshape(a, (3, 1)) * b)

# Add a vector to each row of the matrix
c = np.array([[1, 2, 3], [4, 5, 6]])
print(c + a)
