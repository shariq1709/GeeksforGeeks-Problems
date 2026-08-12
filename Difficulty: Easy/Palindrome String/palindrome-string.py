class Solution:
    def isPalindrome(self, s):
        # code here
        reverse=s[::-1]
        if s==reverse:
            return True
        else:
            return False
