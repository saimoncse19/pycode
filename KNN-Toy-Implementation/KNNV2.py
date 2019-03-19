"""K-NN toy implementation in scientific way,
with using data science tools...
Author: Saimon
email: saimoncse19@gmail.com
Date: March 19, 2019 """

from math import sqrt
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt, style

style.use("ggplot")

file = "mock.csv"
# Reading the CSV as Pandas' DataFrame object
load = pd.read_csv(file, index_col=0)

distance = []

# x, y value of the new object to be classified...
new = [2.2, 3]

# Calculating Euclidean Distance of each point from new point
for i, j in zip(load["x"], load["y"]):
    val = np.linalg.norm(np.array([i, j]) - np.array(new))
    distance.append(round(val, 5))

# adding the distance to our Data Frame
load["distance"] = distance

# Sorting the DataFrame by distance
l = load.sort_values(by=["distance"])

# calculating k and checking if it is odd...
# if it is not odd, we need to add 1 to it
rounded_value = round(sqrt(len(load["x"])))
k = rounded_value if rounded_value % 2 != 0 else (rounded_value + 1)


x1, y1 = [], []
x2, y2 = [], []
for a, b, c in zip(load["x"], load["y"], load["class"]):
    if c == 0:
        x1.append(a)
        y1.append(b)
    else:
        x2.append(a)
        y2.append(b)


# Plotting the initial data set
plt.title("K-NN toy Implementation")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.scatter(x1, y1, label="Class 0", color="red")
plt.scatter(x2, y2, label="Class 1", color="green")


sum0, sum1 = 0, 0

for i in (l["class"])[:k]:
    if i == 0:
        sum0 += 1
    else:
        sum1 +=1

# Plotting the new data point with appropriate labeling
new_class = None
if sum0 > sum1:
    new_class = 0
    plt.plot(new[0], new[1], color="red")
    plt.annotate("Class 0", xy=(new[0]+.2, new[1]+.2), xytext=(new[0]+2, new[1]+2), arrowprops=dict(facecolor='red',
                shrink=0.05, connectionstyle="angle3,angleA=0,angleB=-90"), fontsize=10)

elif sum0 < sum1:
    new_class = 1
    plt.plot(new[0], new[1], color="green")
    plt.annotate("Class 1", xy=(new[0] + .2, new[1] + .2), xytext=(new[0] + 2, new[1] + 2),
                 arrowprops=dict(facecolor='green',
                                 shrink=0.05, connectionstyle="angle3,angleA=0,angleB=-90"), fontsize=10)

plt.legend()
plt.show()
