""" Calculation of Hamming Distance
Author: Saimon
email: saimoncse19@gmail.com
Date: March 21, 2019 """


def hamming_distance(a: str, b: str):

    distance = 0

    if len(a) == len(b):
        for i, j in zip(a, b):
            if i != j:
                distance += 1
        return distance

    else:
        return "The two strings are not of equal size..."


x = hamming_distance("10011010", "10101110")
print(x)
