class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        thisDict = set()
        for n in nums:
            if n in thisDict:
                return True
            thisDict.add(n)
        return False