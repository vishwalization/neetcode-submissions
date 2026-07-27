class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sy = ['+', '-', '*', '/']
        st = []

        for i in tokens:
            if i not in sy:
                st.append(int(i))

            else:
                last = st.pop()
                slast = st.pop()

                if i == '+':
                    st.append(last + slast)
                elif i == '-':
                    st.append(slast - last)
                elif i == '*':
                    st.append(last * slast)
                else:
                    st.append(int(slast / last))

        return st[-1]
                

