import matplotlib.pyplot as plt
import pandas as pd

plt.style.available
plt.style.use("dark_background")


def load_data():
    college = pd.read_csv("data/College.csv", index_col=0).rename_axis("College")
    college["Elite"] = pd.cut(college["Top10perc"], [0, 50, 100], labels=["No", "Yes"])
    college["AcceptRate"] = college["Accept"] / college["Apps"]
    return college


college = load_data()
college.head()

# 8.

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
