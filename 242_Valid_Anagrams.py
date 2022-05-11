class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # #my brute force, compare lens and sort the strings and compare it 
        # if len(s)==len(t) and str("".join(sorted(s))) == str("".join(sorted(t))):
        #         return True
        # else:
        #     return False
        
        #Optimal Solution
        if Counter(s) == Counter(t):
            return True
        
        return False