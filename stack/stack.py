"""Stack implementation
Author: Saimon
email: saimoncse19@gmail.com
Date: March 30, 2019 """


class Stack:

    """
    Stack follows the last-in first-out (LIFO) principle.
    That means the last value added to the stack is the first one to get removed.
    """

    def __init__(self):

        """
        Initializes an empty stack.
        """

        self.list = []

    def push(self, value):

        """
        :param value: value is added to the end of the stack
        :return: None
        """

        self.list += [value]        # self.list.append(value) would do the same

    def pop(self):

        """

        :return: the last value in the stack is removed and returned.
        """

        try:
            x = self.list[-1]
            del self.list[-1]
            return x

        except IndexError:
            print("Stack is empty.")

    def get_top(self):

        try:
            return self.list[-1]

        except IndexError:
            print("Stack is empty.")

    def show_stack(self):

        """
        :return: returns the stack
        """

        return self.list


# Object creation
my_stack = Stack()

# Adding values to list-based Stack
my_stack.push(45)   # [45]
my_stack.push(78)   # now [45, 78]
my_stack.push(47)   # now [45, 78, 47]
print(f"The stack is {my_stack.show_stack()}")

# Getting the last value
print(f"The top(rightmost value) of the stack is {my_stack.get_top()}")

# Removing the last element from the stack and returning it - TWICE

print(f"Popping {my_stack.pop()}")
print(f"Popping {my_stack.pop()}")

# The stack now has only one element. Popping the last element....
print(my_stack.show_stack())
last = my_stack.pop()
print(f"Popping the only remaining element {last}")

# Trying to remove from the empty stack
my_stack.pop()

# Finally, printing the empty stack
print(my_stack.list)
