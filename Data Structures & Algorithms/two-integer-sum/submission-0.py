class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visit = {}

        for i in range(len(nums)):
            to_find = target - nums[i]
            if to_find in visit:
                return [min(visit[to_find], i), max(visit[to_find], i)]
            else:
                visit[nums[i]]=i