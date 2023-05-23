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

    def pop(self) -> int:
        root = self.get_min()
        last_value = self.values.pop()
        if len(self.values) != 0:
            self.values[0] = last_value
            self.sift_down(0)
        return root

    def sift_down(self, index: int):
        if index * 2 + 1 >= self.get_size():
            return
        left_child_index = index * 2 + 1
        right_child_index = left_child_index + 1
        min_child_index = left_child_index
        if right_child_index < self.get_size() and self.values[right_child_index] < self.values[left_child_index]:
            min_child_index = right_child_index
        if self.values[min_child_index] >= self.values[index]:
            return
        self.values[index], self.values[min_child_index] = self.values[min_child_index], self.values[index]
        self.sift_down(min_child_index)

    def print_structure(self):
        index = 0
        step = 1
        size = self.get_size()
        while index < size:
            line = ""
            for i in range(index, min(index + step, size)):
                line += f"{self.values[i]} "
            index += step
            step *= 2
            print(line[:-1])


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
        elif command.startswith("pop"):
            print(heap.pop())
        elif command.startswith("structure"):
            print("---STRUCTURE START---")
            heap.print_structure()
            print("---STRUCTURE END---")
        elif command.startswith("exit"):
            print("bye")
            break
    pass


main()
