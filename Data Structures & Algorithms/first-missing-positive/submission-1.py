class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # num_set = set(nums)
        # for i in range(1,len(nums)+2):
        #     if i not in num_set:
        #         return i

        freq = {}

        for num in nums:
            freq[num] = True

        for i in range(1,len(nums)+2):
            if i not in freq:
                return i





        