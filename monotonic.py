class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        stack = []
        next_smaller = [n] * n
        
        # Step 1: next smaller element index
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                next_smaller[i] = stack[-1]
            
            stack.append(i)
        
        # Step 2: count subarrays
        res = 0
        for i in range(n):
            res += next_smaller[i] - i
        
        return res
