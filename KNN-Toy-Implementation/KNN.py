"""K-NN toy implementation in traditional way,
without using any data science tools...
Author: Saimon
email: saimoncse19@gmail.com
Date: March 19, 2019 """


from math import sqrt

# Our initial data set
data = {
    "x": [4.2, 4.0, 3.8, 2.0, 2.7, 1.7, 2.7, 1.2, 2.2, 0.3],
    "y": [2.8, 2.0, 0.5, 1.5, 2.5, 3.2, 4.0, 5.2, 6.2, 6.2],
    "class": [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
}

distance = []
new = [2.2, 3]
# Calculating Euclidean Distance of each point from new point
for i, j in zip(data["x"], data["y"]):
    val = sqrt((i - new[0])**2 + (j - new[1])**2)
    distance.append(round(val, 5))

# adding the distance to our data set
data["distance"] = distance
# sorting the distance in ascending order
sorted_distance = sorted(distance)

# Calculating K, considering the length of x, y or class from the dataset, we can get k by sqrt(len(x, y or class)
# then we need to round the value and check if the rounded value is odd.
# if it is not odd, we need to add 1 to it
rounded_value = round(sqrt(len(data["x"])))
k = rounded_value if rounded_value % 2 != 0 else (rounded_value + 1)

new_dict = {}
new_x = []
new_y = []
new_class = []

# Calculating the new_x, new_y and new_class with sorted distance
for i in sorted_distance:
    for j in data["distance"]:
        if i == j:
            index = data["distance"].index(j)
            new_x.append(data["x"][index])
            new_y.append(data["y"][index])
            new_class.append(data["class"][index])


# Updating the new dictionary: new_dict
new_dict["x"], new_dict["y"], new_dict["class"] = new_x, new_y, new_class

sum0, sum1 = 0, 0
for i in new_class[:k]:
    if i == 0:
        sum0 += 1
    else:
        sum1 +=1

if sum0 > sum1:
    print("The new object belongs to class 0...")
elif sum0 < sum1:
    print("The new object belongs to class 1...")
    
