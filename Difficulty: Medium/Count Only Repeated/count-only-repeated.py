from collections import Counter
class Solution:
    def findRepeating(self, arr):
        # code here 
        freq=Counter(arr)
        for value,count in freq.items():
            if count>1:
                return (value,count)
        return (-1,-1)