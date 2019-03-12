""" Author: Saimon
Email: Saimoncse19@gmail.com
Date: March 12, 2019 """


def check_a(z: str):

    inc = 0
    for j in range(len(z)):
        if z[j] == "a":
            inc += 1
    if len(z) == inc:
        return True
    else:
        return False


def check_b(z: str):

    inc = 0
    for j in range(len(z)):
        if z[j] == "b":
            inc += 1
    if len(z) != 0 and len(z) == inc:
        return True
    else:
        return False


x = input("Enter something:  ")
y = len(x)

if y == 0:
    print("The empty string is recognised by a*")

elif y == 1 and x == "a":
    print(f"{x} is recognised by a*")
elif y == 1 and x == "b":
    print(f"{x} is recognised by a*b+")
elif y == 2 and (x == "aa"):
    print(f"{x} is recognised by a*")
elif y == 2 and (x == "ab"):
    print(f"{x} is recognised by a*b+")
elif y == 3 and x == "aab":
    print(f"{x} is recognized by aab and a*b+")

elif y >= 3 and check_a(x):
    print(f"{x} is recognized by a*")

elif y >= 3 and not check_a(x):
    for i in x:
        index = x.index(i)
        if i == "b":
            dump_a = x[:index]
            dump_b = x[index:]
            if check_a(dump_a) and check_b(dump_b):
                print(f"{x} is recognized by a*b+...")

            else:
                print("Not Recognized...")
            break
