class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num,0) + 1

        for i in nums:
            if freq.get(i,0) > (len(nums)/2):
                return i


        