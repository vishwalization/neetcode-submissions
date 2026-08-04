class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def lower_bound(self, key, timestamp):
        lis = self.d[key]

        l, r = 0, len(lis) - 1
        ans = -1

        while l <= r:
            mid = l + (r - l) // 2

            if lis[mid][0] <= timestamp:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans
        

    def get(self, key: str, timestamp: int) -> str:
        # finding lower bound
        lb_ts = self.lower_bound(key, timestamp) 

        # if no values return ""
        if lb_ts == -1:
            return ""

        return self.d[key][lb_ts][1]
        
