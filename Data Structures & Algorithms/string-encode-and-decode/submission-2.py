class Solution:

    def encode(self, strs: List[str]) -> str: 
        ''' 
            1. why do we use 4# in between words isn't in part of ascii characters

        '''
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)

        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            l = int(s[i:j])
            i = j + 1
            j = i + l
            res.append(s[i:j])
            i = j

        return res

