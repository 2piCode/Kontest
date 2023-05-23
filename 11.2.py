import ast


def get_common_parent(tree: dict, first_value: int, second_value: int) -> int:
    root_key = list(tree.keys())[0]
    first_parents = get_parents(tree, root_key, first_value, [root_key])
    second_parents = get_parents(tree, root_key, second_value, [root_key])
    return get_common_element(first_parents, second_parents)


def get_parents(tree: dict, key: int, value: int, parents: []) -> []:
    if key not in tree:
        return None
    if value in tree[key]:
        return parents
    for i in tree[key]:
        a = get_parents(tree, i, value, parents + [i])
        if a is not None:
            return a


def get_common_element(a: [], b: []) -> int:
    for i in reversed(a):
        for j in reversed(b):
            if i == j:
                return i


def get_tree_from_str(a: str) -> dict:
    return ast.literal_eval(a)


def main():
    n = int(input())
    tree = get_tree_from_str(input())
    a, b = map(int, input().split())
    parent = get_common_parent(tree, a, b)
    print(parent)


if __name__ == "__main__":
    main()
