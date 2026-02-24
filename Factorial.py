class Solution:
    def factorial(self, n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        
        return [int(digit) for digit in str(result)]
