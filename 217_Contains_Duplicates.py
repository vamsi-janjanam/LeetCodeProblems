class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#         hashset = set()
#         for n in nums:
#             if n in hashset:
#                 return True
#             else:
#                 hashset.add(n)
#         return False
        dict_nums = {}
        for n in nums:
            if n in dict_nums:
                return True
            else:
                dict_nums[n] = True
        return False