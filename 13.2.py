class Node:
    def __init__(self):
        self.is_end = False
        self.count = 0
        self.child = {}


class Trie:
    def __init__(self, words: []):
        self.root = Node()
        for word in words:
            self.add(word)

    def add(self, s: str):
        node = self.root
        for i in s:
            if i not in node.child:
                node.child[i] = Node()
            node = node.child[i]
        node.is_end = True
        node.count += 1

    def get_best_str(self, prefix: str) -> str:
        node = self.get_end_prefix_node(prefix)
        if not node:
            return None
        all_words_with_prefix = []
        self.find_child(node, prefix, all_words_with_prefix)
        words_with_max_count = get_words_with_max_count(all_words_with_prefix)
        if len(words_with_max_count) > 1:
            words_with_max_count.sort(key=lambda word: (len(word), word))
        return words_with_max_count[0]

    def get_end_prefix_node(self, prefix: str) -> Node:
        node = self.root
        if prefix == " ":
            return node
        for i in prefix:
            if i not in node.child:
                return None
            node = node.child[i]
        return node

    def find_child(self, node: Node, word: str, result):
        if node.is_end:
            result.append((word, node.count))
        for char in node.child.keys():
            self.find_child(node.child[char], word + char, result)
        return


def get_words_with_max_count(words: []) -> []:
    max_count = 0
    words_with_max_count = []
    for word, count in words:
        if count > max_count:
            words_with_max_count.clear()
            max_count = count
            words_with_max_count.append(word)
        if count == max_count:
            words_with_max_count.append(word)
    return words_with_max_count


def main():
    words = input().split()
    trie = Trie(words)
    while True:
        inp = input()
        line, *args = inp.split()
        if line.startswith("+"):
            trie.add(args[0])
            print("ok")
        elif line.startswith("?"):
            prefix = " "
            if len(args) > 0:
                prefix = args[0]
            result = trie.get_best_str(prefix)
            if result:
                print(result[1:] if prefix == " " else result)
            else:
                print("None")
        elif line.startswith("exit"):
            print("bye")
            break


main()
