class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        ans = 0

        while l <= r:

            mid = l + (r-l) // 2

            if nums[0] > nums[mid]:
                ans = mid 
                r = mid - 1
            else:
                l = mid + 1

        return nums[ans]
