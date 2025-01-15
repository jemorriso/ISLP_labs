import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import subplots

print("fit a model with", 11, "variables")

# print?

x = [3, 4, 5]
x

y = [4, 9, 7]
x + y

x = np.array([3, 4, 5])
y = np.array([4, 9, 7])

x = np.array([[1, 2], [3, 4]])
x.ndim
x.dtype
x.shape

# np.array?

np.array([[1, 2], [3, 4]], float).dtype

x = np.array([1, 2, 3, 4])
x.sum()
np.sum(x)
np.sqrt(x)
x**2
x**0.5

x = np.array([1, 2, 3, 4, 5, 6])
print("beginning x:\n", x)
x_reshape = x.reshape((2, 3))
print("reshaped x:\n", x_reshape)

print("x before we modify x_reshape:\n", x)
print("x_reshape before we modify x_reshape:\n", x_reshape)
x_reshape[0, 0] = 5
print("x_reshape after we modify its top left element:\n", x_reshape)
print("x after we modify top left element of x_reshape:\n", x)

x_reshape.shape, x_reshape.ndim, x_reshape.T

x = np.random.normal(size=50)
x

y = x + np.random.normal(loc=50, scale=1, size=50)

np.corrcoef(x, y)

# use random seed to make it reproducible
rng = np.random.default_rng(1303)

print(rng.normal(scale=5, size=2))
rng2 = np.random.default_rng(1303)
print(rng2.normal(scale=5, size=2))

rng = np.random.default_rng(3)
y = rng.standard_normal(10)
np.mean(y), y.mean()

# these are all the same
np.var(y), y.var(), np.mean((y - y.mean()) ** 2)

np.sqrt(np.var(y)), np.std(y)

X = rng.standard_normal((10, 3))
X
# these are the same
# means get the mean for each COLUMN, rot row
X.mean(axis=0)
X.mean(0)

# mean for each ROW
X.mean(1)

# ## graphics

fig, ax = subplots(figsize=(8, 8))
x = rng.standard_normal(100)
y = rng.standard_normal(100)
ax.plot(x, y)
plt.show()

# these 2 are the same
fig, ax = subplots(figsize=(8, 8))
ax.plot(x, y, "o")
plt.show()
fig, ax = subplots(figsize=(8, 8))
ax.scatter(x, y, marker="o")
plt.show()

fig, ax = subplots(figsize=(8, 8))
ax.scatter(x, y, marker="o")
ax.set_xlabel("this is the x-axis")
ax.set_ylabel("this is the y-axis")
ax.set_title("Plot of X vs Y")

fig.set_size_inches(12, 3)
fig

fig, axes = subplots(nrows=2, ncols=3, figsize=(15, 5))
axes[0, 1].plot(x, y, "o")
axes[1, 2].scatter(x, y, marker="+")
fig
fig.savefig("output/Figure.png", dpi=400)
fig.savefig("output/Figure.pdf", dpi=200)

# we can keep adding to fig and resaving
axes[0, 1].set_xlim([-1, 1])
fig.savefig("output/Figure_updated.jpg")
fig

# ---

# create an evenly split range of 50 numbers from -pi to pi
x = np.linspace(-np.pi, np.pi, 50)
y = x
f = np.multiply.outer(np.cos(y), 1 / (1 + x**2))

# contour plots
fig, ax = subplots(figsize=(8, 8))
ax.contour(x, y, f)
plt.show()

fig, ax = subplots(figsize=(8, 8))
ax.contour(x, y, f, levels=45)
plt.show()

# heatmap
fig, ax = subplots(figsize=(8, 8))
ax.imshow(f)
plt.show()

# ## sequences and slice notation

seq1 = np.linspace(0, 10, 11)
seq1

seq2 = np.arange(0, 10)
seq2

# ## indexing data

A = np.array(np.arange(16)).reshape((4, 4))
A
# element at 2nd row, 3rd column (0-based index)
A[1, 2]
# 2nd and 4th rows
A[[1, 3]]
# 1st and 3rd columns
A[:, [0, 2]]

# numpy reads this as pairs of i and j indices, NOT submatrix
A[[1, 3], [0, 2]]

# submatrix, 2nd and 4th row, 1st, 3rd, 4th column
A[[1, 3]][:, [0, 2, 3]]
# same
idx = np.ix_([1, 3], [0, 2, 3])
A[idx]

# use python slice notation to get a submatrix
A[1:4:2, 0:3:2]
# same
A[[1, 3]][:, [0, 2]]

# ---

keep_rows = np.zeros(A.shape[0], bool)
keep_rows

keep_rows[[1, 3]] = True
keep_rows

"""
notice the difference here, for vector vs matrix
vector is element access:
"""
keep_rows[[1, 3]] = True

"""
matrix is row access:
"""
A[[1, 3]]
"""
"""

# in python True and False are just 1 and 0
np.all(keep_rows == np.array([0, 1, 0, 1]))

# but they are treated differently in numpy

# same
A[np.array([0, 1, 0, 1])]
A[[0, 1, 0, 1]]
# different, retrieves 2nd and 4th rows of A
A[keep_rows]

# same
keep_rows
np.array([False, True, False, True])
# different
np.array([0, 1, 0, 1])

keep_cols = np.zeros(A.shape[1], bool)
keep_cols[[0, 2, 3]] = True
idx_bool = np.ix_(keep_rows, keep_cols)
A[idx_bool]

"""
Run these to understand how it works 
"""
A
A.shape[1]
A.shape[0]

keep_rows
keep_cols
idx_bool
"""
"""

idx_mixed = np.ix_([1, 3], keep_cols)
A[idx_mixed]

# ## loading data
