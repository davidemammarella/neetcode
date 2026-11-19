class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        candidate = []

        for r in range(len(matrix)):
            if matrix[r][-1] >= target:
                candidate = matrix[r]
                break
        
        if len(candidate)==0:
            return False
        
        L, R = 0, len(candidate)-1
        
        while L<=R:
            M = (L+R)//2
            if candidate[M]>target:
                R=M-1
            elif candidate[M]<target:
                L=M+1
            else:
                return True
        
        return False