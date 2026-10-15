def manual_counter(x):
    d = dict()
    for k in x:
        d[k] = d.get(k,0)+1
    return tuple(sorted(d.items()))
            
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for s in strs:
            key = manual_counter(s)

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())
                
            
    
        
            

        
        