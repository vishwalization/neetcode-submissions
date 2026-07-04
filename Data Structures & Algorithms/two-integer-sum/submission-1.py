class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i in range(len(nums)): # O(n)
            d[nums[i]] = i

        print(d)

        # for each value check if target - value is present in hash map 
        for i in range(len(nums)): # O(n)
            inv = target - nums[i]
            print(i, nums[i], inv)
            if inv in d and d[inv] != i:    # O(1)
                return [i, d[inv]]

        # space complexity: # O(n)