class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for i in nums: # O(n) check 
            if i in s: # O(1) check 
                return True
            else:
                s.add(i)
            
        return False