from collections import Counter
class Solution:
    def getSingle(self, arr):
        # code here 
        frq=Counter(arr)
        for num,i in frq.items():
            if i==1:
                return num