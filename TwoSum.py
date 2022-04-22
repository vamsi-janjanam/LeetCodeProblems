#TwoSum.py

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return[i,j]
        complementmap = dict()
        
        for i in range(len(nums)):
            num = nums[i]
            complement = target-num
            if nums[i] in complementmap:
                return[complementmap[num], i]
            else:
                complementmap[complement] = i
