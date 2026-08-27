from collections import Counter
import math
class Solution:
    def findMajority(self, arr):
        # code here
        result=[]
        n=len(arr)
        freq=Counter(arr)
        for key,value in freq.items():
            if value>math.floor(n/3):
                result.append(key)
        return sorted(result)