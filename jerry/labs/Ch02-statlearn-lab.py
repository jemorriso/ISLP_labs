import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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

Auto = pd.read_csv("Auto.csv")
Auto

Auto = pd.read_csv("Auto.data", delim_whitespace=True)
Auto

Auto["horsepower"]

np.unique(Auto["horsepower"])

Auto = pd.read_csv("Auto.data", na_values=["?"], delim_whitespace=True)
Auto["horsepower"].sum()

Auto.shape

Auto_new = Auto.dropna()
Auto_new.shape

Auto = Auto_new
Auto.columns

# first 3 rows
Auto[:3]

# using a boolean array to return matching rows
idx_80 = Auto["year"] > 80
idx_80
Auto[idx_80]

# column subset
Auto[["mpg", "horsepower"]]

# we did not specify an index when we loaded the data so it's just integers
Auto.index

Auto_re = Auto.set_index("name")
Auto_re
Auto_re.columns
Auto_re.index

rows = ["amc rebel sst", "ford torino"]
# access rows by name now that we set the index
Auto_re.loc[rows]

# similar to numpy
# rows
Auto_re.iloc[[3, 4]]
# columns
Auto_re.iloc[:, [0, 2, 3]]

# rows and columns
Auto_re.iloc[[3, 4], [0, 2, 3]]

Auto_re.loc["ford galaxie 500", ["mpg", "origin"]]

# these do the same
# a
idx_80 = Auto_re["year"] > 80
Auto_re.loc[idx_80, ["weight", "origin"]]
# b is more concise
Auto_re.loc[lambda df: df["year"] > 80, ["weight", "origin"]]

# & is element-wise 'and' operation, | is element-wise 'or'
Auto_re.loc[lambda df: (df["year"] > 80) & (df["mpg"] > 30), ["weight", "origin"]]
Auto_re.loc[
    lambda df: (df["displacement"] < 300)
    & (df.index.str.contains("ford") | df.index.str.contains("datsun")),
    ["weight", "origin"],
]

# > In summary, a powerful set of operations is available to index the rows and columns of data frames. For integer based queries, use the `iloc[]` method. For string and Boolean
# > selections, use the `loc[]` method. For functional queries that filter rows, use the `loc[]` method
# > with a function (typically a `lambda`) in the rows argument.

# ---

rng = np.random.default_rng(1)
A = rng.standard_normal((127, 5))
A

M = rng.choice([0, np.nan], p=[0.8, 0.2], size=A.shape)
M

A += M
A

D = pd.DataFrame(A, columns=["food", "bar", "pickle", "snack", "popcorn"])
D[:3]

for col in D.columns:
    template = 'Column "{0}" has {1:.2%} missing values'
    print(template.format(col, np.isnan(D[col]).mean()))

np.isnan(D["food"])
# we use the mean of the true / false array, which makes sense when you remember they are just ones and zeroes
np.isnan(D["food"]).mean()

# ## Additional Graphical and Numerical Summaries

fig, ax = subplots(figsize=(8, 8))
ax.plot(Auto["horsepower"], Auto["mpg"], "o")
plt.show()

# easier syntax
ax = Auto.plot.scatter("horsepower", "mpg")
ax.set_title("Horsepower vs. MPG")
plt.show()

fig = ax.figure
fig.savefig("output/horsepower_mpg.png")

fig, axes = subplots(ncols=3, figsize=(15, 5))
Auto.plot.scatter("horsepower", "mpg", ax=axes[1])
plt.show()

Auto.cylinders = pd.Series(Auto.cylinders, dtype="category")
Auto.cylinders.dtype

fig, ax = subplots(figsize=(8, 8))
Auto.boxplot("mpg", by="cylinders", ax=ax)
plt.show()

fig, ax = subplots(figsize=(8, 8))
Auto.hist("mpg", ax=ax)
plt.show()

pd.plotting.scatter_matrix(Auto)
plt.show()

pd.plotting.scatter_matrix(Auto[["mpg", "displacement", "weight"]])
plt.show()

Auto[["mpg", "weight"]].describe()

Auto["cylinders"].describe()
Auto["mpg"].describe()
