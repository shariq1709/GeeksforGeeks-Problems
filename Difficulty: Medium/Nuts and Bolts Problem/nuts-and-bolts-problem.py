class Solution:
    def matchPairs(self, nuts, bolts):
        order = ['!', '#', '$', '%', '&', '*', '?', '@', '^']
        nuts_set = set(nuts)
        idx = 0
        for char in order:
            if char in nuts_set:
                nuts[idx] = char
                bolts[idx] = char
                idx += 1