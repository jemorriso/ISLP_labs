import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.available
plt.style.use("dark_background")
plt.style.use("default")

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
