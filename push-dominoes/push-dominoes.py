class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        size = len(dominoes)
        left = [100001] * size
        right = [100001] * size
        tmp_l = -1
        tmp_r = -1
        answer = ''
        
        for i in range(size-1, -1, -1):
            if dominoes[i] == 'L':
                tmp_l = i
            if dominoes[i] == 'R':
                tmp_l = -1
            if dominoes[i] == '.' and tmp_l != -1:
                left[i] = tmp_l - i
                
        for i in range(size):
            if dominoes[i] == 'R':
                tmp_r = i
            if dominoes[i] == 'L':
                tmp_r = -1
            if dominoes[i] == '.' and tmp_r != -1:
                right[i] = i - tmp_r
                
        for i in range(size):
            if left[i] != right[i]:
                if left[i] < right[i]:
                    answer += 'L'
                else:
                    answer += 'R'
            else:
                answer += dominoes[i]
                
        return answer
    