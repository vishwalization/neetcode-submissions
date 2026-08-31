import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        low = [] # max heap
        high = [] # min heap

        for i in (nums1+nums2):
            if not low or i < -low[0]:
                heapq.heappush(low, -i)
            else:
                heapq.heappush(high, i)

            if len(low) > len(high) + 1:
                heapq.heappush(high, -heapq.heappop(low))
            elif len(high) > len(low):
                heapq.heappush(low, -heapq.heappop(high))

        if len(low) > len(high):
            return -low[0]
        
        return (-low[0] + high[0]) / 2.0


        

