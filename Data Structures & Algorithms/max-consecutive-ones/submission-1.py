class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        actual=0
        prev=0

        for i in range(len(nums)):
            if nums[i]==1:
                actual+=1
                if actual>prev:
                    prev=actual
            else:
                actual=0
        
        return prev