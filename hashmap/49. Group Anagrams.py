



from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
            ["cat","atc","leet", "meet", cate, cake]
            method 1 => hashmap for each character 
                {
                    c 
                    a 
                    t
                }
            example: 
                cat => {act: 1}
        """
        map = {}
        result = []
        for ele in strs:
            sortedLetter = str(sorted([ch for ch in ele]))
            # print(sortedLetter, map)
            if sortedLetter in map:
                result[map[sortedLetter]].append(ele)
            else:
                result.append([ele])
                map[sortedLetter] = len(result) - 1
        return result      


soln = Solution()

print(soln.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

    

