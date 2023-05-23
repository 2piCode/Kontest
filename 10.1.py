class Node:
    def __init__(self, value, parent, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.value}"


class Tree:
    def __init__(self, array: [] = None):
        self.root = None
        if array is not None and len(array) > 0:
            self.root = self.form_tree_from_array(array, 0, len(array))

    def form_tree_from_array(self, array: [], left: int, right: int) -> Node:
        if left + 1 > right:
            return None
        if left + 1 == right:
            return Node(array[left], None)
        middle = (left + right - 1) // 2
        node = Node(array[middle], None)
        node.left = self.form_tree_from_array(array, left, middle)
        node.right = self.form_tree_from_array(array, middle + 1, right)
        if node.left is not None:
            node.left.parent = node
        if node.right is not None:
            node.right.parent = node
        return node

    def __str__(self):
        self.print(self.root, [])
        return ""

    def print(self, node: Node, nesting_level: []):
        if node is None:
            return

        deep_str = ""
        nesting_level_count = len(nesting_level)
        if nesting_level_count > 0:
            for i in range(nesting_level_count - 1):
                deep_str += '│   ' if nesting_level[i] else '    '

            deep_str += "├───" if nesting_level[nesting_level_count - 1] else "└───"

        print(f"{deep_str}{node}")
        self.print(node.left, nesting_level + [True])
        self.print(node.right, nesting_level + [False])


def main():
    array = list(map(int, input().split()))
    tree = Tree(array)
    print(tree)


if __name__ == "__main__":
    main()
