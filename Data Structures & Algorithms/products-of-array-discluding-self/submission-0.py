class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        1. given a n bits, how big of a number could be saved in it ? 
        2. immediate idea: O(n^2) approach
        '''
        n = len(nums)
        ans = []
        for i in range(n):
            prod = 1
            for j in range(n):
                if i != j:
                    prod *= nums[j]

            ans.append(prod)

        return ans


        