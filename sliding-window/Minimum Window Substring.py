class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        """
            s="ADOBECODEBANC"
            t="ABC"
            
            
        """

        tmap = {}
        for i in t: 
            tmap[i] = tmap.get(i, 0) + 1
        tlen = len(t)
        
        for ind, ele in enumerate(s):
            if ele in tmap:
                left = ind
                right = ind + 1
                
                if tmap[ele] == 0: del tmap[ele] 
                else: tmap[ele] -= 1
                tlen -= 1
                
                while right < len(s):
                    ch = s[right]
                    if ch in tmap:
                        if tmap[ch] == 0: del tmap[ch] 
                        else: tmap[ch] -= 1
                        tlen -= 1
                        if tlen == 0: return s[left:right + 1]
                    right +=1
                break
        
        return ""
            
        