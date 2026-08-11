class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''

        window, ct = defaultdict(int), defaultdict(int)
        for c in t:
            ct[c] += 1

        have, needed = 0, len(ct)
        res, reslen = [-1,-1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in ct and window[c] == ct[c]:
                have += 1

            while have == needed:
                if r - l + 1 < reslen:
                    res = [l, r]
                    reslen = r - l + 1

                window[s[l]] -= 1
                if s[l] in ct and window[s[l]] < ct[s[l]]:
                    have -= 1
                l += 1

        l, r = res

        return s[l : r + 1] if reslen != float('inf') else ''
