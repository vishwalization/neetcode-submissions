class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        ans = 1

        def time_req(mid):
            t = 0
            for i in piles:
                t += (i // mid if i % mid == 0 else (i//mid + 1))

            return t

        print(time_req(3))


        while l <= r:
            mid = l + (r - l)// 2

            if time_req(mid) > h:
                l = mid + 1
                
            else:
                ans = mid
                r = mid - 1

        return ans
