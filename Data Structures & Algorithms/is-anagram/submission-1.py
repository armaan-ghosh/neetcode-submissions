class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictionS = {}
        dictionT = {}

        for i in s:
            dictionS[i] = 1 + dictionS.get(i,0)
            
        for j in t:
            dictionT[j] = 1 + dictionT.get(j,0)

        if dictionS == dictionT:
            return True
        else:
            return False