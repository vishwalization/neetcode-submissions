class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        maxy = 0
        ans = 0
        l = 0

        for r in range(len(s)):
            d[s[r]] += 1
            maxy = max(maxy, d[s[r]])

            while r - l + 1 - maxy > k:
                d[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)

        return ans