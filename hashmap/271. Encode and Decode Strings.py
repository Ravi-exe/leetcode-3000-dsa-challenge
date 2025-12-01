# need to improvise
from typing import List


class Solution:

    def __init__(self):
        self.encoder = {}
        self.decoder = {}

    def encode(self, strs: List[str]) -> str:
        result: str = ''
        for i in strs:
            if self.encoder.get(i) == None:
                key = "^" + str(len(self.encoder)) + "$"
                self.encoder[i] = key
                self.decoder[key] = i

            result += self.encoder[i]

        return result
            

    def decode(self, s: str) -> List[str]:
        result=[]
        word= ''
        for i in range(len(s)):
            word+=s[i]
            if self.decoder.get(word) != None:
                result.append(self.decoder[word])
                word=''

        return result