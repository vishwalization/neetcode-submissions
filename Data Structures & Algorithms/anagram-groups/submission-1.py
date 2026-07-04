class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list) # space complexity: O(n)

        for i, s in enumerate(strs): # O(n)
            lis = [0] * 26
            for c in s:
                lis[ord(c) - ord('a')] += 1
            hm[tuple(lis)].append(i)        # dict key can't be a dict/list ie mutable

        ans = []
        for list_of_id in hm.values(): # O(n) for both the for loops
            temp = []
            for id in list_of_id:
                temp.append(strs[id])
            ans.append(temp)

        return ans

        