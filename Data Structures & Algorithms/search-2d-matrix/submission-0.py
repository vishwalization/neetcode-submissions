class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def lower_bound(arr):
            l, r = 0, len(arr) - 1
            ans = 0

            while l <= r:
                mid = l + (r - l)//2

                if arr[mid] > target:
                    r = mid - 1
                elif arr[mid] <= target:
                    ans = mid
                    l = mid + 1

            return ans

        row = [matrix[i][0] for i in range(len(matrix))]
        lb = lower_bound(row)

        print(row, lb)

        if row[lb] == target:
            return True

        def bs(arr):
            l, r = 0, len(arr) - 1

            while l <= r:
                mid = l + (r - l)//2

                if arr[mid] > target: 
                    r = mid - 1
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    return True

            return False

        return bs(matrix[lb])
        



