from collections import deque


class DragonDeque:
    def __init__(self):
        self.size = 0
        self.first_part = deque()
        self.second_part = deque()

    def push_left(self, n):
        self.second_part.append(n)
        self.size += 1

    def push_middle(self, n):
        self.second_part.appendleft(n)
        self.size += 1

    def push(self, n):
        self.first_part.appendleft(n)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.first_part.popleft()

    def check_middle(self):
        middle = self.size // 2 + self.size % 2
        if middle > len(self.first_part):
            self.first_part.append(self.second_part.popleft())
        elif middle < len(self.first_part):
            self.second_part.appendleft(self.first_part.pop())


def main():
    dragon_deque = DragonDeque()
    n = int(input())

    for i in range(n):
        dragon_deque.check_middle()
        command = input()
        if command.startswith('-'):
            print(dragon_deque.pop())
        else:
            temp = command.split()
            command, index = temp[0], int(temp[1])
            if command == '+':
                dragon_deque.push_left(index)
            elif command == '*':
                dragon_deque.push_middle(index)
            elif command == '!':
                dragon_deque.push(index)


main()