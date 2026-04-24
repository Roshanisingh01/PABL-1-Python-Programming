class Solution:
    def prevSmaller(self, arr):
        stack = []
        res = []
        
        for x in arr:
            while stack and stack[-1] >= x:
                stack.pop()
            
            if not stack:
                res.append(-1)
            else:
                res.append(stack[-1])
            
            stack.append(x)
        
        return res
