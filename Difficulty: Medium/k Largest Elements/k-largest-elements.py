class Solution:
	def kLargest(self, arr, k):
		# code here
		result=[]
		arr.sort()
		list2=arr[::-1]
		for i in range(k):
		    result.append(list2[i])
		return result
		    