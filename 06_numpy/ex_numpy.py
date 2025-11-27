
import numpy as np
# =====================================================
# 🧩 EXERCISE 1: Create and analyze arrays
# =====================================================
# Create an array 'a' with values [0,1,2,3,4]
a = np.array([0,1,2,3,4])

# Show:
# - The first element
a[0]

# - The object type
type(a)

# - How many elements it has (.size)
a.size

# - Number of dimensions (.ndim)
a.ndim

# - Its shape (.shape)
a.shape


# =====================================================
# 🧩 EXERCISE 2: Indexing and slicing
# =====================================================
# Create array c = np.array([20,1,2,3,4])
c = np.array([20,1,2,3,4])

# Change the first value to 100
c[0] = 100

# Create a new variable d containing values from index 1 to 3
d = c[1:4]

# Change the last two values of array c to 300 and 400
c[3:5] = 300, 400


# =====================================================
# 🧩 EXERCISE 3: Basic vector operations
# =====================================================
# Create arrays a=[1,2,3] and b=[4,5,6]
a = np.array([1,2,3])
b = np.array([4,5,6])

# Compute:
# - a + b
# - a * b

c = a + b
c

d = a * b
d


# =====================================================
# 🧩 EXERCISE 4: Dot product
# =====================================================
# Create u=[1,2,3] and v=[4,5,6]
# Compute their dot product

u = np.array([1,2,3])
v = np.array([4,5,6])
r = np.dot(u, v)


# =====================================================
# 🧩 EXERCISE 5: Add a constant to an array
# =====================================================
# Create s = np.array([1,2,3,-1])
# Add 1 to all elements

s = np.array([1,2,3,-1])
r = s + 1


# =====================================================
# 🧩 EXERCISE 6: Mean and max value
# =====================================================
# Create a = np.array([1,-1,1,-1])
# Compute the mean and the maximum

a = np.array([1,-1,1,-1])
m = a.mean()

mx = a.min()


# =====================================================
# 🧩 EXERCISE 7: np.sin() and np.pi
# =====================================================
# Create array x = np.array([0, np.pi/2, np.pi])
# Compute the sine of each value

x = np.array([0, np.pi/2, np.pi])
z = np.sin(x)


# =====================================================
# 🧩 EXERCISE 8: Create a wave using np.linspace() and np.sin()
# =====================================================
# Create 100 values between 0 and 2π using np.linspace()
# Compute y = np.sin(x)
# Then plot the wave using plt.plot()

"""
import matplotlib.pyplot as plt
ls = np.linspace(1, 10, 100)
x = np.sin(ls)

y = plt.plot(ls, x)
plt.title("Sine Wave")
plt.xlabel("Angle (radians)")
plt.ylabel("Height (sin(x))")
plt.grid(True)
plt.show()
"""


# =====================================================
# 🧩 EXERCISE 9: Standard deviation
# =====================================================
# Create a = np.array([10,20,30])
# Compute mean and standard deviation

da = v.std()

v = np.array([10,20,30])
md = v.mean()


# =====================================================
# 🧩 EXERCISE 10: Plot vectors with matplotlib
# =====================================================
# Use function Plotvec1(u, z, v) to draw 3 vectors:
# u=[1,0], v=[0,1], z = u + v
"""
u = np.array([1, 0])
v = np.array([0, 1])
z = u + v
def Plotvec1(a, b, c):
    origin = np.zeros(2)
    plt.quiver(*origin, *a, angles='xy', scale_units='xy', scale=1, color='r', label='u')
    plt.quiver(*origin, *b, angles='xy', scale_units='xy', scale=1, color='g', label='z')
    plt.quiver(*origin, *c, angles='xy', scale_units='xy', scale=1, color='b', label='v')

    plt.xlim(-1, 3)
    plt.ylim(-1, 3)
    plt.grid(True)
    plt.legend()
    plt.show()

u = np.array([1, 0])
v = np.array([0, 1])
z = u + v
Plotvec1(u, z, v)
"""


######################################################
############### WITHOUT HELP #########################
######################################################

# =====================================================
# 🔥 EXERCISE 1: Arrays and properties
# =====================================================
# Create an array with 6 elements and show:
# - First and last value
# - Size, dimensions, and shape

my_array = np.array([1,2,3,4,5,6])
my_array

my_array[0]
my_array[-1]
my_array.ndim
my_array.size
my_array.shape


# =====================================================
# 🔥 EXERCISE 2: Indexing and slicing
# =====================================================
# Create an array from 0 to 9
# Extract values from 3 to 7 into another variable
# Change the last two values to 99 and 100

nw = np.array([0,1,2,3,4,5,6,7,8,9])
vls = nw[3:8]
vls

vls[3:5] = [99,100]
vls


# =====================================================
# 🔥 EXERCISE 3: Vector operations
# =====================================================
# Create two arrays and compute:
# - Addition
# - Multiplication
# - Dot product
# - Add a constant

px = np.array([29,34,1,245,2,1,34,9])
pz = np.array([11,43,22,18,99,3,2,1])

pxz = px + pz
pxz2 = px * pz
px1 = px + 1


# =====================================================
# 🔥 EXERCISE 4: Universal functions
# =====================================================
# Create an array with positive and negative values
# Compute mean, max and standard deviation

pp = np.array([-2,32,1,-43, 81])
pp.mean()
pp.max()
pp.std()


# =====================================================
# 🔥 EXERCISE 5: Waves and plots
# =====================================================
# Create a sine wave with np.linspace() and np.sin()
# Plot the wave with matplotlib
# Then create a cosine wave and plot both in the same graph

"""
x = np.linspace(0, 10 * np.pi, 50000)
y = np.sin(x)
plt.plot(x, y)
"""


# =====================================================
# 🔥 EXERCISE 6: Vector visualization
# =====================================================
# Draw vectors u, v and z using Plotvec1
# Example:
# u=[1,1], v=[-1,0], z=u+v

"""
u = np.array([1, 1])
v = np.array([-1, 0])
z = u + v
Plotvec1(u, v, z)
"""


# =====================================================
# 🔥 EXERCISE 7: 2D arrays
# =====================================================
# Create a 2x3 matrix with values from 1 to 6
# Show:
# - Number of dimensions
# - Shape
# - Total size

matriz = np.array([[1, 2, 3],
                   [4, 5, 6]])

matriz.shape
matriz.std()
matriz.size
type(matriz)
matriz.ndim


# =====================================================
# 🔥 EXERCISE 8: Advanced np.linspace
# =====================================================
# Create 50 values between 0 and 10 using np.linspace()
# Compute np.sin(x) and np.cos(x)
# Plot both functions together with different colors

"""
nv = np.linspace(0,10,50)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.plot(y_sin, y_cos)
"""


# =====================================================
# 🔥 EXERCISE 9: Visual standard deviation
# =====================================================
# Create array [10,20,30,40]
# Compute its mean and standard deviation
# Plot the values as points and draw a horizontal line for the mean

"""
arrayf = np.array([10,20,30,40])
arr = arrayf.mean()
stt = arrayf.std()

plt.scatter(range(len(arrayf)), arrayf, color='b')
plt.axhline(arr)
plt.show()
"""


# =====================================================
# 🔥 EXERCISE 10: Combined plots
# =====================================================
# Use plt.subplot() to show two graphs:
# 1) A sine wave
# 2) A cosine wave
# Both created with np.linspace()

"""
import numpy as np

x = np.linspace(0, 10, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.subplot(1, 2, 1)
plt.plot(x, y_sin)

plt.subplot(1, 2, 2)
plt.plot(x, y_cos)

plt.show()
"""


