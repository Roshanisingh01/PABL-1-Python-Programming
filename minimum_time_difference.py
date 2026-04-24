class Solution:
    def minDifference(self, arr):
        times = []
        
        # convert HH:MM:SS → seconds
        for t in arr:
            h, m, s = map(int, t.split(':'))
            total = h*3600 + m*60 + s
            times.append(total)
        
        times.sort()
        
        ans = float('inf')
        
        # check adjacent
        for i in range(1, len(times)):
            ans = min(ans, times[i] - times[i-1])
        
        # circular check (midnight wrap)
        ans = min(ans, 86400 - times[-1] + times[0])
        
        return ans
