import heapq
from typing import List

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)

        total = sum(nums)
        target = total / 2
        reduced = 0
        operations = 0

        while reduced < target:
            x = -heapq.heappop(heap)
            half = x / 2

            reduced += half
            heapq.heappush(heap, -half)
            operations += 1

        return operations
