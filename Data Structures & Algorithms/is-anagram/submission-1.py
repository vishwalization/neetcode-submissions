class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t) # O(n + m)

        # space complexity: O(1) since 26 keys at most