class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1

        maxA = 0

        while l < r:
            lHeight = heights[l] 
            rHeight = heights[r]

            a = min(lHeight, rHeight) * (r-l)
            maxA = max(a, maxA)

            if lHeight <= rHeight:
                l+=1
            else:
                r-=1
        return maxA

        