class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = Counter(nums)

        l = []
        for num, freq in hm.items():
            l.append((freq, num))

        l.sort()

        ans = []
        for i in range(len(l) - 1, len(l) - k - 1, -1):
            ans.append(l[i][1])

        return ans
