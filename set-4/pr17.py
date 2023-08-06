# 17. **Implement Trie (Prefix Tree)**: Implement a trie with insert, search, and startsWith methods.
#     - *Input*: insert("apple"), search("apple"), startsWith("app")
#     - *Output*: "True, True"


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Test the trie
trie = Trie()
trie.insert("apple")

print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: False
print(trie.startsWith("app"))  # Output: True
