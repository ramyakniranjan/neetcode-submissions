class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # num_set = set(nums)
        # for i in range(1,len(nums)+2):
        #     if i not in num_set:
        #         return i


        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) + 1

        for i in range(1,len(nums)+2):
            if freq.get(i,0) == 0:
                return i





        