"""Double-ended queue (Deque) implementation
Author: Saimon
email: saimoncse19@gmail.com
Date: March 31, 2019 """


class Deque:

    """
    Deque supports addition and removal of objects from both ends.
    """

    def __init__(self):

        """
        Initializes an empty deque.
        """

        self.deque = []

    def add_first(self, value):

        """
        :param value: value is added to the head of the deque
        :return: None
        """

        self.deque.insert(0, value)

    def add_last(self, value):

        """
        :param value: value is added to the tail of the deque
        :return: None
        """

        self.deque.append(value)

    def remove_first(self):

        """
        :return: the first value in the deque is removed and returned.
        """

        try:
            x = self.deque[0]
            del self.deque[0]
            return x

        except IndexError:
            print("Deque is empty.")

    def remove_last(self):

        """
        :return: the last value in the deque is removed and returned.
        """

        try:
            x = self.deque[-1]
            del self.deque[-1]
            return x

        except IndexError:
            print("Deque is empty.")

    def get_head(self):

        try:
            return self.deque[0]

        except IndexError:
            print("Deque is empty.")

    def get_tail(self):

        try:
            return self.deque[-1]

        except IndexError:
            print("Deque is empty.")

    def show_deque(self):

        """
        :return: returns the deque
        """

        return self.deque

    def length(self):
        """returns the length of the deque"""
        return len(self.deque)

    def is_empty(self):

        if self.length() == 0:
            return True

        else:
            return False


# Object creation
my_deque = Deque()

# The Deque is initially empty, so my_deque.is_empty() returns True
print(f"Is my deque empty? --> {my_deque.is_empty()}")

# Adding values to list-based deque
my_deque.add_first(45)   # [45]
my_deque.add_first(78)   # now [78, 45]
my_deque.add_last(47)   # now [78, 45, 47]

print(f"The length of the deque is --> {my_deque.length()}")
print(f"The deque is now {my_deque.show_deque()}")


# The Deque now has 3 elements, so my_deque.is_empty() returns False
print(f"Is my deque empty? --> {my_deque.is_empty()}")


# Getting the tail
print(f"The tail of the deque is {my_deque.get_tail()}")

# Getting the head
print(f"The head of the deque is {my_deque.get_head()}")

# Performing removal of elements

print(f"Removing {my_deque.remove_first()}")   # now [45, 47]
print(f"Removing {my_deque.remove_last()}")    # now [45]

# The Deque now has only one element. Removing the only remaining element...
print(f"The deque now is --> {my_deque.show_deque()}")
last = my_deque.remove_first()        # my_deque.remove_last() would do the same
print(f"Removing the only remaining element --> {last}")

# Trying to remove from the empty deque
my_deque.remove_first()

# Finally, printing the empty deque
print(my_deque.show_deque())
