class Solution:
    def mergeArrays(self, mat):
        result = []
        for row in mat:
            result.extend(row)
        result.sort()
        return result