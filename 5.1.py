import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Deque:
    def __init__(self):
        self.size = 0
        self.head = None
        self.last = None

    def push(self, n):
        if self.size == 0:
            self.head = self.last = Node(n)
            self.size += 1
        else:
            self.last.next = Node(n)
            self.last = self.last.next
            self.size += 1

    def pop(self):
        if self.size == 1:
            result = self.head.value
            self.head = self.last = None
            self.size = 0
            return result
        else:
            result = self.head.value
            self.head = self.head.next
            self.size -= 1
            return result

    def view(self):
        temp = self.head
        while temp.next is not None:
            print(temp.value, end=', ')
            temp = temp.next
        print(temp.value)

    def clear(self):
        self.head = self.last = None
        self.size = 0


def main():
    deque = Deque()

    while True:
        line = sys.stdin.readline()
        if line.startswith("push"):
            n = line.split()[1]
            deque.push(n)
            print("ok")
        elif line.startswith("pop"):
            print(f"{deque.pop()}")
        elif line.startswith("front"):
            print(f"{deque.head.value}")
        elif line.startswith("size"):
            print(f"{deque.size}")
        elif line.startswith("view"):
            deque.view()
        elif line.startswith("clear"):
            deque.clear()
            print("ok")
        elif line.startswith("exit"):
            print("bye")
            break


main()
