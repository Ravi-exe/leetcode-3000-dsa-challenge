
from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        
        """
            Input: 
            board = [
              ["A","B","C","D"],
              ["S","A","A","T"],
              ["A","C","A","E"]
            ],
            word = "CAT"

            Output = True
        """
        
        i_len = len(board)
        for i in range(i_len):
            j_len = len(board[i])
            for j in range(j_len): 
                ch = board[i][j]
                if ch == word[0]:
                    route = set()
                     
                    def recurse(i, j, ind=1):
                        
                        # print(i, j, ind)
                        if ind == len(word): 
                            return True
                        
                        route.add((i, j))
                        if i != 0 and word[ind] == board[i-1][j] and not (i-1,j) in route:
                            result = recurse(i-1, j, ind+1)
                            if result == True: return True
                        if i != i_len - 1 and word[ind] == board[i+1][j] and not (i+1,j) in route:
                            result = recurse(i+1, j, ind+1)
                            if result == True: return True
                        if j != 0 and word[ind] == board[i][j-1] and not (i,j-1) in route:
                            result = recurse(i, j-1, ind+1)
                            if result == True: return True
                        if j != j_len - 1 and word[ind] == board[i][j+1] and not (i,j+1) in route:
                            result = recurse(i, j+1, ind+1)
                            if result == True: return True
                        route.remove((i,j))
                        
                        return False
                    
                    result = recurse(i, j, 1)
                    if result == True: return True
        
        return False