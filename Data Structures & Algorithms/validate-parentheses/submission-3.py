class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ')': '(',
            ']': '[',
            '}': '{'
            }

        st = []
        for i in s:
            if i in mp:
                if st and st[-1] == mp[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)

        return st == []
                
            