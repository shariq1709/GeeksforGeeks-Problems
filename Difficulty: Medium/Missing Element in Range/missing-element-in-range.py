class Solution:
    def missingRange(self, arr, low, high):
        #code here
        result=[]
        arr_set=set(arr)
        for i in range(low,high+1):
            if i not in arr_set:
                result.append(i)
        return result