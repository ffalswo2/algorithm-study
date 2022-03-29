class Node:
    def __init__(self, value= ""):
        self.value = value
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        curr_node = self.root

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(curr_node.value + char)
            curr_node = curr_node.children[char]

    def has(self, string):
        curr_node = self.root

        for char in string:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        return True

trie = Trie()
trie.insert("cat")
trie.insert("can")

print(trie.has("cat"))
print(trie.has("can"))
print(trie.has("cap"))