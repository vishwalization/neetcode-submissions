class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = []
        for c in s:
            if c.isalnum():
                l.append(c.lower())

        l = ''.join(l)

        i, j = 0, len(l) - 1
        while i < j:
            if l[i] != l[j]:
                return False

            i += 1
            j -= 1

        return True