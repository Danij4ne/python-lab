
import numpy as np

# we create a list/array using numpy and it works the same way as in Python
a = np.array([0,1,2,3,4])  

print(a[0])  # result 0

print(type(a))  # numpy.ndarray

a.size  # tells you how many elements it has (5)

a.ndim  # result 1, means it is a one-dimensional array (a simple list)

# example: 2-dimensional array
b = np.array([[1, 2, 3],
              [4, 5, 6]])

print(b.ndim)  # result 2

a.shape  # shows how many elements are in each dimension → (5,)


# indexing and slicing methods
c = np.array([20,1,2,3,4])

c[0] = 100  # we change the value at position 0 to 100

d = c[1:4]  # we take values from index 1 to 3 (1,2,3) and store them in d

c[3:5] = 300, 400  # we change values 3 and 4 in c


# basic operations

# vector addition
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = a + b
print(result)  # [5 7 9]

u=[1,0]
v=[0,1]
z=[]

for n, m in zip(u, v):  # zip() pairs elements from both lists; without numpy we would do this to get the same result
    z.append(n + m)


# vector multiplication
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = a * b
print(result)  # [4 10 18]

u = [1, 0]
v = [0, 1]
z = []

for n, m in zip(u, v):  # same idea but multiplying instead of adding
    z.append(n * m)

print(z)  # [0, 0]


# np.dot()
# takes two vectors of the same size and returns a single number (scalar)

# example
u = [1, 2, 3]
v = [4, 5, 6]

# dot product:
# (1×4) + (2×5) + (3×6) = 4 + 10 + 18 = 32

import numpy as np

u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

result = np.dot(u, v)
print(result)  # 32


# adding constants to a numpy array
s = np.array([1,2,3,-1])

w = u + 1
# operation: 1+1 , 2+1 , 3+1 , -1+1
# result:
w = [2,3,4,0]


# universal functions

# calculate the average value of all elements (mean())
a = np.array([1,-1,1,-1])
mean_a = a.mean()

"""
a = [1, -1, 1, -1]

Total = 1 + (-1) + 1 + (-1) = 0
Elements = 4
Mean = 0 / 4 = 0
"""

# find maximum value
b = np.array([1,-2,3,4,5])
max_b = b.max()  # returns 5


# pi
np.pi  # value of π = 3.141592653589793


x = np.array([0, np.pi/2, np.pi])  # angles in radians
# x = [0, 1.57079633, 3.14159265]

y = np.sin(x)  # sine for each angle
# y = [0, 1, 0]


# linspace() creates evenly spaced numbers inside a range
# np.linspace(start, end, number_of_values)

x = np.linspace(0, 10, 5)
# result:
r = [0, 2.5, 5, 7.5, 10]


# example:
x = np.linspace(0, 2*np.pi, 100)  # from 0 to 6.28... with 100 values

# wave height
y = np.sin(x)  # wave oscillation (0 → 1 → -1 → 0)

"""
if using Jupyter Notebook, use:

%matplotlib inline

plt.plot(x, y) → plots the graph
x = horizontal axis values
y = vertical axis values
"""


# a.dtype → numeric type of array elements
print(a.dtype)
# result = int64

# type(a) → type of the whole object


# std() → standard deviation, how far values are from the mean

a = np.array([10, 10, 10, 10])
print(a.std())  # 0.0 → all values are equal

a = np.array([10, 20, 30])
print(a.mean())  # 20
print(a.std())   # 8.16 standard deviation


"""
import matplotlib.pyplot as plt

def Plotvec1(u, z, v):
    ax = plt.axes()  # creates a canvas with X/Y axes

    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)  # draws vector u
    plt.text(*(u + 0.1), 'u')  # label

    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)  # vector v
    plt.text(*(v + 0.1), 'v')

    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)  # vector z = u + v
    plt.text(*(z + 0.1), 'z')

    plt.ylim(-2, 2)  # graph limits
    plt.xlim(-2, 2)
"""





