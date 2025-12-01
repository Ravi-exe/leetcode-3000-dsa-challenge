from typing import Dict



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map: Dict[str, int] = {}
        for i in s:
            map[i] = map.get(i, 0) 
        for i in t:
            if map.get(i) == None or map[i] == 0:
                return False
            map[i] = map[i] - 1
        return True
    
