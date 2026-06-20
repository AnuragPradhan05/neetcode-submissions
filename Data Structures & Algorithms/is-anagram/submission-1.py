class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = {}
        freqT = {}
        for ch1 in s:
            freqS[ch1] = freqS.get(ch1,0) + 1
            
        for ch2 in t:
            freqT[ch2] = freqT.get(ch2,0) + 1


        for key in freqS:
            if freqS.get(key) != freqT.get(key) or len(s) != len(t):
                return False
        return True



