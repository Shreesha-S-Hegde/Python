import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

arr = np.array(42)
print(arr)

#2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

#3D array
arr = np.array([[['a', 'b', 'c'], ['d', 'e', 'f']], [['g', 'h', 'i'], ['j', 'k', 'l']]])
print(arr)

#Check number of dimensions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)