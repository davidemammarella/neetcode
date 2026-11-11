class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNumber = 0
        countNumber = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                countNumber += 1
            if nums[i] == 0 and maxNumber <= countNumber:
                maxNumber = countNumber
                countNumber = 0
            elif nums[i] == 0:
                countNumber = 0
        if maxNumber <= countNumber:
            maxNumber = countNumber
        return maxNumber