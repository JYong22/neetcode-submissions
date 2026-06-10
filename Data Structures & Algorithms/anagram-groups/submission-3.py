class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ret = []
        thisDict = {}


        for s in strs:
            sortedWord = ''.join(sorted(s))
            if sortedWord in thisDict:
                thisDict[sortedWord].append(s)
            else:
                thisDict[sortedWord] = [s]
        
        for values in thisDict.values():
            ret.append(values)
        return ret
        