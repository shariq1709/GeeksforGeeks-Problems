from collections import Counter

class Solution:
    def firstRepeated(self, arr):
        freq = Counter(arr)
        for i in range(len(arr)):
            if freq[arr[i]] > 1:
                return i + 1  
        return -1