class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()
        
        def canPlace(mid):
            count = 1
            last = arr[0]
            
            for i in range(1, len(arr)):
                if arr[i] - last >= mid:
                    count += 1
                    last = arr[i]
                
                if count >= k:
                    return True
            
            return False
        
        left, right = 0, arr[-1] - arr[0]
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if canPlace(mid):
                ans = mid
                left = mid + 1   # try bigger
            else:
                right = mid - 1
        
        return ans
