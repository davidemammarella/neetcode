class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        LEN = len(nums)
        ans=[0]*(2*LEN)

        for i in range(LEN):
            ref = LEN+i
            ans[i]=nums[i]
            ans[ref]=nums[i]
        
        return ans