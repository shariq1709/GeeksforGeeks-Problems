from collections import Counter

class Solution:
    def topKFreq(self, arr, k):
        freq = Counter(arr)
        pairs = []
        for number, count in freq.items():
            pairs.append((count, number))
        pairs.sort(reverse=True)
        return [number for count, number in pairs[:k]]