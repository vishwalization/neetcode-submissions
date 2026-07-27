class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)

        st = []

        for i in range(len(temperatures)):
            while st and temperatures[st[-1]] < temperatures[i]: # current element > previous
                ans[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)

        return ans