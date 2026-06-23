class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        # fixed sliding window
        initial = {}
        thisDict = {}
        for i in range(26):
            initial[chr(ord('a') + i)] = 0
            thisDict[chr(ord('a') + i)] = 0

        for i in range(len(s1)):
            initial[s1[i]] = 1 + initial.get(s1[i], 0)
            thisDict[s2[i]] = 1 + thisDict.get(s2[i], 0)

        if initial == thisDict:
            return True


        l = 0
        for r in range(len(s1), len(s2)):
            thisDict[s2[l]] -= 1
            thisDict[s2[r]] += 1
            l+=1
            if thisDict == initial:
                return True
        

        return False


        