from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
         return nums * 2  
    
#solution

solution = Solution()
nums = [1, 2, 3]
result = solution.getConcatenation(nums)
print(result)