class Node:
    def __init__(self, capacity, price):
        self.capacity = capacity
        self.price = price

    def __lt__(self, other):
        return self.price / self.capacity < other.price / other.capacity

    def __gt__(self, other):
        return self.price / self.capacity > other.price / other.capacity

    def __le__(self, other):
        return self.price / self.capacity <= other.price / other.capacity

    def __ge__(self, other):
        return self.price / self.capacity >= other.price / other.capacity



class Heap:
    def __init__(self):
        self.values = []

    def get_size(self) -> int:
        return len(self.values)

    def get_min(self) -> Node:
        return self.values[0]

    def add(self, value: Node):
        index = len(self.values)
        self.values.append(value)
        self.sift_up(index)

    def sift_up(self, index: int):
        if index == 0:
            return
        parent_index = (index - 1) // 2
        if self.values[index] > self.values[parent_index]:
            self.values[index], self.values[parent_index] = self.values[parent_index], self.values[index]
            self.sift_up(parent_index)

    def pop(self) -> Node:
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
        if right_child_index < self.get_size() and self.values[right_child_index] > self.values[left_child_index]:
            min_child_index = right_child_index
        if self.values[min_child_index] <= self.values[index]:
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


def get_max_price(package_capacity: int, cakes: Heap) -> float:
    price = 0.0
    while cakes.get_size() > 0:
        node = cakes.pop()
        if package_capacity < node.capacity:
            price_by_unit_volume = node.price / node.capacity
            piece_price = package_capacity * price_by_unit_volume
            price += piece_price
            break
        else:
            price += node.price
            package_capacity -= node.capacity
    return price


def main():
    heap = Heap()
    count_cakes, package_capacity = map(int, input().split())
    for i in range(count_cakes):
        price, capacity = map(int, input().split())
        heap.add(Node(capacity, price))
    cost = get_max_price(package_capacity, heap)
    print(f"{cost:.2f}")


main()
