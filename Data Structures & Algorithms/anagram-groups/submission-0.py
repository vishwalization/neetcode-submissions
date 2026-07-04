class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for i, s in enumerate(strs):
            lis = [0] * 26
            for c in s:
                lis[ord(c) - ord('a')] += 1
            hm[tuple(lis)].append(i)

        ans = []
        for list_of_id in hm.values():
            temp = []
            for id in list_of_id:
                temp.append(strs[id])
            ans.append(temp)

        return ans