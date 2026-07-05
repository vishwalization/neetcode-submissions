class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        1. given a n bits, how big of a number could be saved in it ? 
        2. immediate idea: O(n^2) approach
        3. learnt the division approach 
            - compute prod of non zero elements, zero count 
            - if count > 1 return 0
            - if count == 0 return prod/ nums[i]
            - if count == 1 return 0 if nums[i] > 0 else return prod
        '''

        prod, zerocnt = 1, 0
        for i in nums:
            if i: 
                prod *= i
            else:
                zerocnt += 1

        if zerocnt > 1: 
            return [0] * len(nums)

        ans = [0] * len(nums)
        for i, n in enumerate(nums):
            if zerocnt:
                ans[i] = 0 if n else prod
            else:
                ans[i] = prod // n

        return ans
                

