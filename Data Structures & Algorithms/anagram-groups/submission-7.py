class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ret = []
        thisDict = {}


        for s in strs:
            newS = "".join(sorted(s))
            if newS in thisDict:
                thisDict[newS].append(s)
            else:
                thisDict[newS] = [s]
        

        for v in thisDict.values():
            ret.append(v)
        
        return ret