"""
Author: Saimon
Email: saimoncse19@gmail.com

"""


class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = Node()

        self.__size = 0

    def insert(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new
        self.__size += 1

    def deletion(self):
        if self.head.value:
            self.head = self.head.next
            self.__size -= 1
        else:
            print('Linked list is empty...')

    @property
    def size(self):
        return self.__size


if __name__ == '__main__':
    link = SinglyLinkedList()
    print(link.head.value, link.size)
    link.insert(5)
    print(link.head.value, link.size)
    link.insert(7)
    print(link.head.value, link.size)
    link.deletion()
    print(link.head.value, link.size)
    link.deletion()
    link.deletion()








