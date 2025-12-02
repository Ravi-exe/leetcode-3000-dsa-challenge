
from typing import Any, Dict, List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        hmap: Dict[str, Any] = {
            "h": {},
            "v": {},
            "c": {
                1: {1: {}, 2: {}, 3: {}},
                2: {1: {}, 2: {}, 3: {}},
                3: {1: {}, 2: {}, 3: {}},
            }
        }
        for indX, value in enumerate(board):
            for indY, valueData in enumerate(value):
                if valueData == ".": 
                    continue
                cubeX= 1 if indX >= 0 and indX <= 2 else 2 if indX >=3 and indX <=5 else 3 
                cubeY= 1 if indY >= 0 and indY <= 2 else 2 if indY >=3 and indY <=5 else 3 
                print(cubeX, cubeY, indX, indY, hmap)
                if ((hmap["h"].get(indX) and hmap["h"][indX].get(valueData) != None) or 
                    (hmap["v"].get(indY) and hmap["v"][indY].get(valueData) != None) or 
                    (hmap["c"][cubeX][cubeY].get(valueData) != None)):
                    return False

                hmap["h"].setdefault(indX, {})[valueData] = 1
                hmap["v"].setdefault(indY, {})[valueData] = 1
                hmap["c"][cubeX][cubeY][valueData] = 1


        return True


