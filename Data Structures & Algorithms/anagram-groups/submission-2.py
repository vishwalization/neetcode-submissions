class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list) # space complexity: O(n)

        for s in strs: # O(n * m)
            lis = [0] * 26
            for c in s:
                lis[ord(c) - ord('a')] += 1

            hm[tuple(lis)].append(s)        # dict key can't be a dict/list ie mutable

        return list(hm.values())

        
        