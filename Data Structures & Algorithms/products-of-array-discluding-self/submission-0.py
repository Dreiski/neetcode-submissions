class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        total = 1
        temp = 0
        zero_cnt = 0

        for x in nums:
            if x:
                total *= x
            else:
                zero_cnt += 1
            
        if zero_cnt > 1: return [0] * n
        
        res = [0] * n
        for i, c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else total
            else: res[i] = total // c
                
            
        return res
        