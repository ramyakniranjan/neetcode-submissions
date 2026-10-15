class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #---dictionary---#
        # d = dict()
        # for k in nums:
        #     if k in d:
        #         d[k] += 1
        #         if d[k] > 1: 
        #             return True
        #     else:
        #         d[k] = 1
        # return False

        # d = dict()
        # for k in nums:
        #     d[k] = d.get(k,0)+1
        # if d[k] > 1:
        #     return True
        # else:
        #     return False


        #---count---#
        from collections import Counter
        cnt = Counter(nums)
        if not cnt:
            return False
        else: 
            return max(cnt.values()) > 1
      
       
     
        #---using set----#
        # if len(nums) == len(set(nums)):
        #     return False
        # else:
        #     return True
        