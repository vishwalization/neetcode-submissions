class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(arr):
            l, r = 0, len(arr) - 1
            ans = 0

            while l <= r:
                mid = l + (r - l) // 2

                if nums[0] > nums[mid]:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return ans

        def bs(arr, l, r):
            while l <= r:
                mid = l + (r - l ) // 2

                if arr[mid] > target:
                    r = mid - 1
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    return mid
            return -1

        pivot = find_pivot(nums)
        if pivot == 0:
            return bs(nums, 0, len(nums)-1)

        flag = target >= nums[0]

        return bs(nums, 0, pivot-1) if flag else bs(nums, pivot, len(nums) - 1)



