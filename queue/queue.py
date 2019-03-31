"""Queue implementation
Author: Saimon
email: saimoncse19@gmail.com
Date: March 31, 2019 """


class Queue:

    """
    Queue follows the first-in first-out (FIFO) principle.
    That means the first value added to the stack is the first one to get removed.
    """

    def __init__(self):

        """
        Initializes an empty queue.
        """

        self.queue = []

    def enqueue(self, value):

        """
        :param value: value is added to the end of the queue
        :return: None
        """

        self.queue += [value]        # self.queue.append(value) would do the same

    def dequeue(self):

        """
        :return: the first value in the queue is removed and returned.
        """

        try:
            x = self.queue[0]
            del self.queue[0]
            return x

        except IndexError:
            print("Queue is empty.")

    def get_head(self):

        try:
            return self.queue[0]

        except IndexError:
            print("Queue is empty.")

    def get_tail(self):

        try:
            return self.queue[-1]

        except IndexError:
            print("Queue is empty.")

    def show_queue(self):

        """
        :return: returns the queue
        """

        return self.queue

    def length(self):
        """returns the length of the queue"""
        return len(self.queue)


# Object creation
my_queue = Queue()

# Adding values to list-based Queue
my_queue.enqueue(45)   # [45]
my_queue.enqueue(78)   # now [45, 78]
my_queue.enqueue(47)   # now [45, 78, 47]
print(f"The Queue is {my_queue.show_queue()}")
print(f"The length of the queue is {my_queue.length()}")

# Getting the tail
print(f"The tail of the queue is {my_queue.get_tail()}")

# Performing Dequeue operation - TWICE

print(f"Removing {my_queue.dequeue()}")
print(f"Removing {my_queue.dequeue()}")

# The Queue now has only one element. Removing the last element....
print(f"The queue now is --> {my_queue.show_queue()}")
last = my_queue.dequeue()
print(f"Removing the only remaining element --> {last}")

# Trying to remove from the empty queue
my_queue.dequeue()

# Finally, printing the empty queue
print(my_queue.show_queue())
