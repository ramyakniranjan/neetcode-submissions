from collections import Counter
# def manual_counter(x):
#     d = dict()
#     for k in x:
#         d[k] = d.get(k,0)+1
#     return d

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return (manual_counter(s) == manual_counter(t))
        if Counter(s) == Counter(t):
            return True
        else:
            return False
        
        