class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        answer = {}
        wordList = set(wordList)
        
        if endWord not in wordList:
            return list(answer)
        
        arr_ch = [chr(i) for i in range(ord("a"), ord("z") + 1)]
        answer[beginWord] = [[beginWord]]
        
        if beginWord in wordList:
            wordList.remove(beginWord)
        
        while answer:
            newLayer = collections.defaultdict(list)
            for key in answer:
                if key == endWord:
                    return answer[key]
                for i in range(len(key)):
                    for ch in arr_ch:
                        word = key[:i] + ch + key[i+1:]
                        if word in wordList:
                            newLayer[word] += [arr + [word] for arr in answer[key]]
                            
            wordList -= set(newLayer.keys())
            answer = newLayer

        return list(answer)
    