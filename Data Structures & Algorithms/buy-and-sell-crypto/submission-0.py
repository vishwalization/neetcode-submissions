class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        st = []

        ans = 0

        for i in prices:
            if not st:
                st.append(i)

            else:
                if st[-1] > i:
                    st.pop()
                    st.append(i)
                else:
                    ans = max(ans, i - st[-1])

        return ans
