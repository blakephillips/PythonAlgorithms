class TrieNode:

    def __init__(self, content: str, flag: bool = False, child=None):
        self.children = {}

        if child:
            self.children[child.content] = child

        self.content = content
        self.flag = flag

    def getChildren(self):
        return self.children

    def addChild(self, child):
        self.children[child.content] = child


class Trie:

    def __init__(self):

        self.root = TrieNode("*")

    def insert(self, word: str) -> None:
        current_node = self.root

        for character in word:
            if character not in current_node.getChildren():
                new_node = TrieNode(character)

                current_node.addChild(new_node)
                current_node = new_node

            else:
                current_node = current_node.getChildren()[character]

        current_node.flag = True

    def findEndNode(self, word: str) -> TrieNode:

        current_node = self.root

        for character in word:
            if character in current_node.getChildren():
                current_node = current_node.getChildren()[character]
            else:
                return None

        return current_node

    def search(self, word: str) -> bool:
        node = self.findEndNode(word)
        return node.flag if node else False

    def startsWith(self, prefix: str) -> bool:
        node = self.findEndNode(prefix)
        return True if node else False

