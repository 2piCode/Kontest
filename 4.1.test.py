class Node:
    value: int

    def __init__(self, value: int = 0, previous=None):
        self.value = value
        self.previous = previous
        self.next = None


class LinkedList:
    head: Node
    last: Node
    size: int
    capacity: int

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

    def push(self, n: int):
        if self.capacity == 0:
            return
        if self.size == 0:
            self.head = Node(n)
            self.last = self.head
            self.size += 1
            return
        if self.size == self.capacity:
            self.head = self.head.next
            self.head.previous = None
            self.size -= 1
        self.last.next = Node(n, self.last)
        self.last = self.last.next
        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return 0
        self.size -= 1
        if self.size == 0:
            result = self.head.value
            del self.head
            del self.last
            return result

        result = self.last.value
        self.last = self.last.previous
        return result


def main():
    result = []
    with open("input.txt", "r") as input:
        capacity = int(input.readline())
        list = LinkedList(capacity)

        while True:
            line = input.readline()
            a = line.strip().split(" ")
            if not line or a[0] == "exit":
                result.append("bye")
                break
            elif a[0] == "count":
                result.append(f"{list.size}\n")
            elif a[0] == "pop":
                result.append(f"{list.pop()}\n")
            elif a[0] == "push":
                list.push(int(a[1]))
                result.append("ok\n")

    with open("output.txt", "w") as output:
        for i in result:
            output.write(i)


if __name__ == "__main__":
    main()
