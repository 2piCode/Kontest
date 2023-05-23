import sys
from collections import deque


def main():
    items = deque()

    while True:
        line = sys.stdin.readline()
        if line.startswith("push"):
            n = line.split()[1]
            items.append(n)
            print("ok")
        elif line.startswith("pop"):
            print(f"{items.popleft()}")
        elif line.startswith("front"):
            print(f"{items[0]}")
        elif line.startswith("size"):
            print(f"{len(items)}")
        elif line.startswith("view"):
            print(", ".join(items))
        elif line.startswith("clear"):
            items.clear()
            print("ok")
        elif line.startswith("exit"):
            print("bye")
            break


main()
