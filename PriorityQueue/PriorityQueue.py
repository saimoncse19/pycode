"""
Author: Saimon
Email: saimoncse19@gmail.com

"""


class PriorityQueue:

    def __init__(self):
        self.__priority_queue = set()

    def add(self, key, value):
        self.__priority_queue.add((key, value))

    def top(self):
        if self.length > 0:
            return sorted(self.__priority_queue)[0]

    def pop(self):
        if self.length > 0:
            x = self.top()
            self.__priority_queue.remove(x)
            return x

    def is_empty(self):
        return self.length == 0

    @property
    def length(self):
        return len(self.__priority_queue)


if __name__ == '__main__':
    pQueue = PriorityQueue()
    print(pQueue.is_empty(), pQueue.length, pQueue.top())
    pQueue.add(5, 1010)
    pQueue.add(2, 10155)
    pQueue.add(4, 1080)
    pQueue.add(2, 10101)
    print(pQueue.is_empty(), pQueue.length, pQueue.top())
    print(pQueue.pop())
    print(pQueue.is_empty(), pQueue.length, pQueue.top())




