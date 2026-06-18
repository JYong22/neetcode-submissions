class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # First we have a substring so this is a sliding window
        # Second we cant have duplicate characters so a hashmap is needed

        l = 0
        thisDict = {}
        maxSize = 0
        for r in range(len(s)):
            thisDict[s[r]] = 1 + thisDict.get(s[r], 0)
            if thisDict[s[r]] > 1:
                while thisDict[s[r]] > 1:
                    thisDict[s[l]] = thisDict.get(s[l]) -1
                    l += 1
            else:
                maxSize= max(r - l + 1, maxSize)

        return maxSize
        