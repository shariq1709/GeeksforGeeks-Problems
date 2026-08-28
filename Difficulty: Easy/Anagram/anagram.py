class Solution:
    def areAnagrams(self, s1, s2):
        list1=list(s1)
        list2=list(s2)
        if sorted(list1)==sorted(list2):
            return True
        else:
            return False