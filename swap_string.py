class Solution:
    def minSwaps(self, s1, s2):
        if s1.count('1') != s2.count('1'):
            return -1
        
        count01 = 0
        count10 = 0
        
        for i in range(len(s1)):
            if s1[i] == '0' and s2[i] == '1':
                count01 += 1
            elif s1[i] == '1' and s2[i] == '0':
                count10 += 1
        
        return max(count01, count10)
