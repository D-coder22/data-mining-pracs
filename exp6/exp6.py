import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.plotting import parallel_coordinates
import seaborn as sns

df = pd.read_csv('./iris.csv')

fig = plt.figure(figsize=(10, 7))

# 1D Histogram
ax1 = fig.add_subplot(321)
data = df["sepal length"]
ax1.hist(data, bins=20, color="blue", rwidth=0.7)
ax1.set_title("1D Histogram")
ax1.set_xlabel("Sepal Lengths")
ax1.set_ylabel("Count")

# 2D Histogram
ax2 = fig.add_subplot(322, projection='3d')
data1 = df["sepal length"].to_list()
data2 = df["sepal width"].to_list()
hist, xedges, yedges = np.histogram2d(data1, data2, bins=20)
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)

dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()

ax2.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')
ax2.set_title("2D Histogram")
ax2.set_xlabel("Sepal Length")
ax2.set_ylabel("Sepal width")

# Box plot
fig.add_subplot(3, 2, 3)
data = df.drop("class", axis=1)
data.boxplot()
plt.title("Box Plot")

# Scatter Plot
fig.add_subplot(3, 2, 4)
data1 = df["sepal length"]
data2 = df["petal length"]
plt.scatter(data1, data2)
plt.grid()
plt.title("Scatter Plot")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")

# Parallel Coordinate Plot
fig.add_subplot(3, 2, 5)
parallel_coordinates(df, 'class', color=['g', 'm', 'b'])
plt.title("Parallel Coordinates")

# Correlation Matrix
fig.add_subplot(3, 2, 6)
data = df.drop("class", axis=1)
plt.matshow(data.corr(), fignum=0)
plt.title("Correlation Matrix")

plt.subplots_adjust(hspace=0.5)
plt.show()
plt.close(fig)

# Multiple Scatter plot
sns.pairplot(df, kind="scatter", hue="class")
plt.show()
