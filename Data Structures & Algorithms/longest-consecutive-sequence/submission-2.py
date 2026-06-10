class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        ret = 0
        thisSet = set(nums)
        
        for n in nums:
            currSequence = 1
            i = n
            while i + 1 in thisSet:
                currSequence +=1
                i +=1
            ret = max(ret, currSequence)

        return ret