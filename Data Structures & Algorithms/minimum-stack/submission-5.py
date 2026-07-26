class MinStack:

    def __init__(self):
        self.st = []
        self.mins = []
        

    def push(self, val: int) -> None:
        if not self.mins or self.mins[-1] >= val: # self.mins[-1] > val gave wrong answer as it ignores duplicate min values
            self.mins.append(val)
        self.st.append(val)
        

    def pop(self) -> None:
        if self.mins and self.mins[-1] == self.top():
            self.mins.pop()
        self.st.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]

        
