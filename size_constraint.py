class Solution:
    def equalPartition(self, arr):
        n = len(arr)
        total = sum(arr)
        
        target = total // 2
        
        # size constraint
        sizes = [n // 2]
        if n % 2 == 1:
            sizes.append((n + 1) // 2)
        
        res = []
        used = [False] * n
        
        def backtrack(start, path, curr_sum, size):
            if len(path) == size:
                if curr_sum == target:
                    return path[:]
                return None
            
            for i in range(start, n):
                if curr_sum + arr[i] > target:
                    continue
                
                path.append(i)
                ans = backtrack(i + 1, path, curr_sum + arr[i], size)
                if ans:
                    return ans
                path.pop()
            
            return None
        
        for sz in sizes:
            idxs = backtrack(0, [], 0, sz)
            if idxs:
                subset1 = [arr[i] for i in idxs]
                subset2 = [arr[i] for i in range(n) if i not in idxs]
                return [subset1, subset2]
        
        return []
