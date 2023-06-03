class Node:
    def __init__(self):
        self.is_banned = False
        self.child = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, s: str):
        node = self.root
        for i in s:
            if i not in node.child:
                node.child[i] = Node()
            node = node.child[i]
        node.is_banned = True

    def check_correctness_word(self, s: str) -> int:
        node = self.root
        is_banned = False
        count = 0
        for i in s:
            if i not in node.child:
                node = self.root
                count += 1
                continue

            node = node.child[i]
            if node.is_banned:
                is_banned = True
                break

        return -1 if not is_banned else count


def main():
    n = int(input())
    trie = Trie()
    for i in range(n):
        ban_word = input().lower()
        trie.add_word(ban_word)

    m = int(input())
    is_banned = False
    line_num = -1
    index = -1
    for i in range(m):
        line = input().lower()
        if is_banned:
            continue
        line_array = line.split(" ")
        count = 0
        for word in line_array:
            ban_index = trie.check_correctness_word(word)
            if ban_index != -1:
                is_banned = True
                line_num = i + 1
                index = count + 1 + ban_index
                break
            count += len(word) + 1

    if not is_banned:
        print("Одобрено")
    else:
        print(f"{line_num} {index}")


main()
