class Solution:
    def count(self, s):
        freq = [0] * 26
        
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        ans = 0
        
        for x in freq:
            if x > 0 and x % 2 == 0:
                ans += 1
                
        return ans
