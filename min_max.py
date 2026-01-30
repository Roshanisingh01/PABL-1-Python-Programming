class Solution:
    def getMinMax(self, arr):
        minimum = arr[0]
        maximum = arr[0]

        for i in arr:
            if i < minimum:
                minimum = i
            if i > maximum:
                maximum = i

        return [minimum, maximum]
