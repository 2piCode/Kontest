class Heap:
    def __init__(self):
        self.values = []

    def get_size(self) -> int:
        return len(self.values)

    def get_min(self) -> int:
        return self.values[0]

    def add(self, value: int):
        index = len(self.values)
        self.values.append(value)
        self.sift_up(index)

    def sift_up(self, index: int):
        if index == 0:
            return
        parent_index = (index - 1) // 2
        if self.values[index] < self.values[parent_index]:
            self.values[index], self.values[parent_index] = self.values[parent_index], self.values[index]
            self.sift_up(parent_index)


def main():
    heap = Heap()
    while True:
        command = input()
        if command.startswith("add"):
            value = int(command.split()[1])
            heap.add(value)
            print("ok")
        elif command.startswith("min"):
            print(heap.get_min())
        elif command.startswith("size"):
            print(heap.get_size())
        elif command.startswith("exit"):
            print("bye")
            break
    pass


main()
