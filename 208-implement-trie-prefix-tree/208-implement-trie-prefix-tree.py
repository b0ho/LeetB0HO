class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
            
        trie["isEnd"] = True 

    def search(self, word: str) -> bool:
        trie = self.trie
        
        for char in word:
            if char in trie:
                trie = trie[char]
            else:
                return False
        
        if "isEnd" in trie:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        
        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return False
            
        return True
