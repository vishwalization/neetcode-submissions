class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        1. given a n bits, how big of a number could be saved in it ? 
        2. immediate idea: O(n^2) approach
        3. learnt the division approach 
            - compute prod of non zero elements, zero count 
            - if count > 1 return 0
            - if count == 0 return prod/ nums[i]
            - if count == 1 return 0 if nums[i] != 0 else return prod
        4. learnt the prefix and suffix approach
        '''

        # approach 4

        n = len(nums)
        p, s = [0] * n, [0] * n

        p[0] = s[n-1] = 1

        for i in range(1, n):
            p[i] = p[i - 1] * nums[i-1]

        for i in range(n - 2, -1, -1):
            s[i] = s[i + 1] * nums[i + 1]

        return [p[i] * s[i] for i in range(n)] 

        # approach 3
        # prod, zerocnt = 1, 0
        # for i in nums:
        #     if i: 
        #         prod *= i
        #     else:
        #         zerocnt += 1

        # if zerocnt > 1: 
        #     return [0] * len(nums)

        # ans = [0] * len(nums)
        # for i, n in enumerate(nums):
        #     if zerocnt:
        #         ans[i] = 0 if n != 0 else prod
        #     else:
        #         ans[i] = prod // n

        # return ans
                

