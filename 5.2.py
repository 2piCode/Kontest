import sys
from collections import deque


class Node:
    def __init__(self, value: int, importance: int):
        self.value = value
        self.importance = importance


def push(items: deque, index: int, importance: int):
    item = Node(index, importance)
    index = len(items)
    for i, elem in enumerate(items):
        if elem.importance < item.importance:
            index = i
            break
    items.insert(index, item)


def pop(items: deque, importance: int):
    result = -1
    if len(items) == 0:
        return -1
    for item in items:
        if item.importance == importance:
            items.remove(item)
            result = item.value
            break

    return result


def pop_all(items: deque, importance: int):
    if len(items) == 0:
        return -1
    result = []
    temp = pop(items, importance)
    while temp != -1:
        result.append(temp)
        temp = pop(items, importance)
    length = len(result)
    if length == 0:
        return -1
    return ' '.join(map(str, result))


def main():
    items = deque()

    while True:
        line = sys.stdin.readline()
        if line.startswith("push"):
            temp = line.split()
            push(items, int(temp[1]), int(temp[2]))
            print("ok")
        elif line.startswith("pop top"):
            if len(items) == 0:
                print(-1)
            else:
                print(items.popleft().value)
        elif line.startswith("popall"):
            print(pop_all(items, int(line.split()[1])))
        elif line.startswith("pop"):
            print(pop(items, int(line.split()[1])))
        elif line.startswith("size"):
            print(f"{len(items)}")
        elif line.startswith("clear"):
            items.clear()
            print("ok")
        elif line.startswith("exit"):
            print("bye")
            return


main()
