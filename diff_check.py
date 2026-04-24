class Solution:
    def minDifference(self, arr):
        # Convert time string to seconds
        def toSeconds(t):
            h, m, s = map(int, t.split(":"))
            return h * 3600 + m * 60 + s
        
        n = len(arr)
        times = []
        
        for t in arr:
            times.append(toSeconds(t))
        
        # Sort times
        times.sort()
        
        ans = float('inf')
        
        # Check adjacent differences
        for i in range(1, n):
            ans = min(ans, times[i] - times[i - 1])
        
        # Check circular difference (midnight wrap)
        ans = min(ans, 86400 - times[-1] + times[0])
        
        return ans
