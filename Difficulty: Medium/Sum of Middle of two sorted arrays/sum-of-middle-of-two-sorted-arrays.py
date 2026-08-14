class Solution:
    def findMidSum(self, arr1, arr2):
        # code here
        arr1.extend(arr2)
        result=sorted(arr1)
        n=len(result)
        if n%2==0:
            return result[(n//2)-1]+result[n//2]