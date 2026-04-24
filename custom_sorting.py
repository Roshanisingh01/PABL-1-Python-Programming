class Solution:
    def frequencySort(self, s):   # 👈 EXACT name
        from collections import Counter
        
        freq = Counter(s)
        
        chars = sorted(freq.keys(), key=lambda x: (freq[x], x))
        
        result = []
        for ch in chars:
            result.append(ch * freq[ch])
        
        return "".join(result)
