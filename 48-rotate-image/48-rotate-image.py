class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        arr = []
        for i in matrix:
            for j in i:
                arr.append(j)
    
        print(arr)
        
        idx = 0
        
        for i in reversed(range(len(matrix))):
            for j in (range(len(matrix[0]))):
                matrix[j][i] = arr[idx]
                idx += 1
        
        print(matrix)