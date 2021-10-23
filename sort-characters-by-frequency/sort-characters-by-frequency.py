class Solution:
    def frequencySort(self, s: str) -> str:
        dict1 = {}
        lst = list(s)
        # print(lst)
        
        for i in lst:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        # print(dict1)
        
        dict2 = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
        
        # print(dict2)
        
        ans = ""
        for i in dict2:
            tmp = i[1]
            while tmp > 0:
                tmp -= 1
                ans += i[0]
        
        return ans
        
        
        
        