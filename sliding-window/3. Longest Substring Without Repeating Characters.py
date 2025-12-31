



from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            find the longest contiouns non duplicate substring
            s = "zxyzxyz"
            
                z   x   y   z   y   z

            using brute force method => 
                time complexity n^2 
                space n

            using pointer we can achieve linear complexity

            using left starting point
            and right is the iteration of string
        """        
        map = {}
        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] in map:
                left = max(map[s[right]] + 1, left)
            map[s[right]] = right
            res = max(res, right - left + 1)
        return res



soln = Solution()

print(soln.lengthOfLongestSubstring("zxyzxyz"))
print(soln.lengthOfLongestSubstring("abcdefgh"))