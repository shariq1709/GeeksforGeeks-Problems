import sys

# Increase Python's string-to-int conversion limit to handle 10^5 digits
sys.set_int_max_str_digits(200000)
class Solution:
	def findSum(self, s1, s2):
		# code here
		num1=int(s1)
		num2=int(s2)
		total=num1+num2
		return str(total)