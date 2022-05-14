class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_map = {}
        for next_str in strs:
            sorted_str = ''.join(sorted(next_str))
            if sorted_str not in string_map:
                string_map[sorted_str] = []
            string_map[sorted_str].append(next_str)
        return list(string_map.values())
        

#         res = defaultdict(list)
#         for i in strs:
#             count = collections.Counter(i).items()
#             count= sorted(count)
#             count = tuple(count)
#             res[count].append(i)
#         return res.values()
