from collections import deque


class Stack:
    items: deque

    def __init__(self, capacity: int):
        self.items = deque(maxlen=capacity)

    def push(self, n: int):
        self.items.append(n)

    def pop(self) -> int:
        return self.items.pop()


def main():
    result = []
    with open("input.txt", "r") as input:
        capacity = int(input.readline())
        stack = Stack(capacity)

        while True:
            line = input.readline()
            a = line.strip().split(" ")
            if not line or a[0] == "exit":
                result.append("bye")
                break
            elif a[0] == "count":
                result.append(f"{len(stack.items)}\n")
            elif a[0] == "pop":
                result.append(f"{stack.pop()}\n")
            elif a[0] == "push":
                stack.push(int(a[1]))
                result.append("ok\n")

    with open("output.txt", "w") as output:
        for i in result:
            output.write(i)


if __name__ == "__main__":
    main()
