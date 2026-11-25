class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        visit={}

        for i in range(len(nums)):
            if nums[i] in visit:
                return True
            else:
                visit[nums[i]]=True
        
        return False