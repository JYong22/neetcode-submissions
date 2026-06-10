class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0 
        right = len(numbers) -1

        while left < right:
            leftN = numbers[left]
            rightN = numbers[right]
            if leftN + rightN == target:
                return [left+1, right+1]
            elif leftN + rightN < target:
                left +=1
            else:
                right -=1
        
        return [0]
        