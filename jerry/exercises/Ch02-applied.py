import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.available
plt.style.use("dark_background")


# 8.


def load_college_data():
    college = pd.read_csv("data/College.csv", index_col=0).rename_axis("College")
    college["Elite"] = pd.cut(college["Top10perc"], [0, 50, 100], labels=["No", "Yes"])
    college["AcceptRate"] = college["Accept"] / college["Apps"]
    return college


college = load_college_data()
college.head()

college = pd.read_csv("data/College.csv")
college.head()

college2 = pd.read_csv("data/College.csv", index_col=0)
college2.head()

college3 = college.rename({"Unnamed: 0": "College"}, axis=1)
college3.head()

college3 = college3.set_index("College")
college3.head()

college = college3
college.head()

college.describe()

college[["Top10perc", "Apps", "Enroll"]]

pd.plotting.scatter_matrix(college[["Top10perc", "Apps", "Enroll"]])
plt.show()

# doesn't work properly with dark background
plt.style.use("default")
college.boxplot("Outstate", by="Private")
plt.show()

# this is provided in the book, but doesn't work
college["Elite"] = pd.cut(college["Top10perc"], [0, 0.5, 1], labels=["No", "Yes"])

# these work
college["Elite"] = pd.cut(college["Top10perc"], bins=2, labels=["No", "Yes"])
college["Elite"], bins = pd.cut(
    college["Top10perc"], bins=2, labels=["No", "Yes"], retbins=True
)
# but we can see that the bins are not the same!
bins

# the reason it didn't work is because they are in percents 🙈
college["Elite"] = pd.cut(college["Top10perc"], [0, 50, 100], labels=["No", "Yes"])

college["Elite"].value_counts()

college.boxplot("Outstate", by="Elite")
plt.show()

plt.style.use("dark_background")
college["Apps"].plot.hist(bins=100)
plt.show()

college["Enroll"].plot.hist(bins=100)
plt.show()

college["Top10perc"].plot.hist(bins=20)
plt.show()

college["Top25perc"].plot.hist(bins=20)
plt.show()

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
college["Top10perc"].hist(ax=ax1, bins=20)
college["Top25perc"].hist(ax=ax2, bins=20)
ax1.set_title("Top 10%")
ax2.set_title("Top 25%")
plt.show()

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
college["Top10perc"].hist(ax=ax1, bins=20)
college["Top25perc"].hist(ax=ax2, bins=20)
ax1.set_title("Top 10%")
ax2.set_title("Top 25%")
plt.show()

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
college["Top10perc"].hist(ax=ax1, bins=20)
college["Top25perc"].hist(ax=ax2, bins=20)
college["Apps"].hist(ax=ax3, bins=20)
college["Enroll"].hist(ax=ax4, bins=20)
ax1.set_title("Top 10%")
ax2.set_title("Top 25%")
ax3.set_title("Applications")
ax4.set_title("Enrollment")
plt.tight_layout()
plt.show()

college["Grad.Rate"].hist(bins=20)
plt.show()

college["PhD"].hist(bins=20)
plt.show()

college["Outstate"].hist(bins=20)
plt.show()

# these are all positively correlated which makes sense.
pd.plotting.scatter_matrix(college[["Apps", "Accept", "Enroll"]])
plt.show()

# you reach extremely high percentages of Top25perc before Top10perc catches up.
pd.plotting.scatter_matrix(college[["Top10perc", "Top25perc"]])
plt.show()

# Top10perc and Outstate are positively correlated.
# Top10perc and AcceptRate are negatively correlated.
pd.plotting.scatter_matrix(college[["Outstate", "AcceptRate", "Top10perc"]])
plt.show()

# Top10perc and Grad.Rate are positively correlated.
pd.plotting.scatter_matrix(college[["Grad.Rate", "AcceptRate", "Top10perc"]])
plt.show()

# 9.


def load_auto_data():
    auto = pd.read_csv("Auto.csv")
    return auto


auto = load_auto_data()
np.unique(auto["horsepower"])

# a. origin and name are the only qualitative variables.

# b and c.

# don't need to do this, just use `describe`
for var in [
    "mpg",
    "cylinders",
    "displacement",
    "horsepower",
    "weight",
    "acceleration",
    "year",
]:
    print(var)
    min = np.min(auto[var])
    max = np.max(auto[var])
    print(f"{'range:':<10}{max - min:>8.2f}")
    print(f"{'mean:':<10}{np.mean(auto[var]):>8.2f}")
    print(f"{'std dev:':<10}{np.std(auto[var]):>8.2f}")
    print()

auto.describe()

# desc is a dataframe
desc = auto.describe()
desc.loc["max", "mpg"] - desc.loc["min", "mpg"]

range_values = desc.loc["max"] - desc.loc["min"]
range_values

# even simpler:
# Method 1: Select only numeric columns
range_values = (
    auto.select_dtypes(include=["number"]).max()
    - auto.select_dtypes(include=["number"]).min()
)
range_values

# Method 2: Drop the 'name' column explicitly
range_values = auto.drop("name", axis=1).max() - auto.drop("name", axis=1).min()
range_values

# d.

auto[0:9]
auto[85:]

# wrong
auto[0:9] + auto[85:]

auto_new = pd.concat([auto[0:9], auto[85:]])

auto_new.drop("name", axis=1).mean()
auto_new.drop("name", axis=1).std()
auto_new.drop("name", axis=1).max() - auto_new.drop("name", axis=1).min()

# e.

# strong correlations here
pd.plotting.scatter_matrix(auto[["mpg", "cylinders", "displacement", "horsepower"]])
plt.show()

pd.plotting.scatter_matrix(auto[["mpg", "weight"]])
plt.show()

pd.plotting.scatter_matrix(auto[["mpg", "acceleration"]])
plt.show()

# steady improvements in mpg year over year
pd.plotting.scatter_matrix(auto[["mpg", "year"]])
plt.show()

# muscle car era 💪
pd.plotting.scatter_matrix(auto[["horsepower", "year"]])
plt.show()

pd.plotting.scatter_matrix(auto[["horsepower", "acceleration"]])
plt.show()

# f.
# displacement, horsepower, cylinders, weight, year would be good variables because they show good explanatory power because they are correlated.
