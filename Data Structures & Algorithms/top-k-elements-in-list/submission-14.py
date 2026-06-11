class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        thisDict = {}

        for n in nums:
            if n in thisDict:
                thisDict[n] += 1
            else:
                thisDict[n] = 1
        print(thisDict)

        sorted_dict = dict(sorted(thisDict.items(), key=lambda x: x[1], reverse=True))

        ret = []
        count = 0
        for keys in sorted_dict.keys():
            if count == k:
                break;
            ret.append(keys)
            count+=1
            

        return ret



        
        