from collections import Counter
class Solution:
    def majorityElement(self, arr):
        #code here
        freq=Counter(arr)
        n=len(arr)
        for i,count in freq.items():
            if count>n//2:
                return i
        return -1