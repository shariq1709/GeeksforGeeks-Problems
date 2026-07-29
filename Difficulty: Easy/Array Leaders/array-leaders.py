class Solution:
    def leaders(self, arr):
        result = []
        n = len(arr)
        max_from_right = arr[-1]
        result.append(max_from_right)

        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right:
                max_from_right = arr[i]
                result.append(arr[i])

        return result[::-1]