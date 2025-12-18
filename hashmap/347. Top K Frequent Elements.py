

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            [1,2,2,11,1,1,1,10]
            
            ele, rank, score, 
            ele freq
            score update
            rank manipulte

            score{
                1: rank ind 0
                2: rank ind 1
                3: rank ind 2
                4: rank ind 3
            }
            rank [(1,10),(2,9),(3,8),(4,7)]
                   1,  2, 3,  4,



        """
        map = {}
        rank = []
        for i in nums:
            print(i, map, rank)
            rank_ind = map.get(i)
            if rank_ind != None:
                rank[rank_ind] = (rank[rank_ind][0], rank[rank_ind][1] + 1)
                while 0 <= rank_ind - 1 and rank[rank_ind - 1][1] < rank[rank_ind][1]:
                        # rank[rank_ind - 1], rank[rank_ind] = rank[rank_ind], rank[rank_ind -1]
                        # map[rank[rank_ind-1][0]] = rank_ind
                        # map[rank[rank_ind][0]]
                        # rank_ind -=1

                        prevRank = rank[rank_ind - 1]
                        currentRank = rank[rank_ind]
                        
                        map[rank[rank_ind][0]] = rank_ind - 1
                        map[rank[rank_ind - 1][0]] = rank_ind
                        rank[rank_ind - 1] = currentRank
                        rank[rank_ind] = prevRank

                        rank_ind -=1
                        
            else:
                rank.append((i,1))
                map[i] = len(rank) - 1
        return [rank[i][0] for i in range(k)]
    


soln = Solution()

print(soln.topKFrequent([1,2,2,11,1,1,1,10],2))
