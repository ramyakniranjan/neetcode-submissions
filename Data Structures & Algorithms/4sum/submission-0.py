class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        equals = set()
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue    
            for j in range(i+1,n-2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                k = j+1 #left pointer
                l = n-1 #right pointer

                while k < l:
                    current_sum = nums[i] + nums[j] +  nums[k] + nums[l]
                    if current_sum == target:
                        equals.add((nums[i], nums[j], nums[k], nums[l]))
                        k = k + 1
                        l = l - 1

                        while k < l and nums[k] == nums[k - 1]:
                            k += 1

                        while k < l  and nums[l] == nums[l + 1]:
                            l -= 1
                    
                    elif current_sum < target:
                        k = k + 1

                    else:           #(current_sum > target)
                        l = l - 1
                    
        return [list(quads) for quads in equals]
            
            
            