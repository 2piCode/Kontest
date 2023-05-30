class Node:
    def __init__(self):
        self.is_end = False
        self.child = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, s: str):
        node = self.root
        for i in s:
            if i not in node.child:
                node.child[i] = Node()
            node = node.child[i]
        node.is_end = True

    def get(self, prefix: str, x: int) -> []:
        node = self.root
        all_words_with_prefix = []
        for i in prefix:
            if i not in node.child:
                return []
            node = node.child[i]

        self.find_child(node, prefix, x, all_words_with_prefix)

        result = []
        for word in all_words_with_prefix:
            if len(word) > len(prefix):
                result.append(word)

        return sorted(result)[:x]

    def find_child(self, node: Node, word: str, x, result):
        if node.is_end:
            result.append(word)
        for char in node.child.keys():
            self.find_child(node.child[char], word + char, x, result)
        return


def main():
    trie = Trie()
    while True:
        line, *args = input().split()
        if line.startswith("add"):
            trie.add(args[0])
            print("ok")
        elif line.startswith("get"):
            result = trie.get(args[0], int(args[1]))
            if len(result) == 0:
                print("empty")
            else:
                print(*result)
        elif line.startswith("exit"):
            print("bye")
            break


main()
