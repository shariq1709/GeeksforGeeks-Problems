class Solution:
    def getSecondLargest(self, arr):
         set1=set(arr)
         result=sorted(set1)
         if len(set1)==1:
             return -1
         else:
             return result[-2]
