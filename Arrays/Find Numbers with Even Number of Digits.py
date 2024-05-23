from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            if len(str(nums[i])) % 2 == 0:
                count += 1
        return count
    
#Solution:
solution = Solution()
nums = [12, 345, 2, 6, 7896]
result = solution.findNumbers(nums)
print(f"The number of integers with an even number of digits is: {result}")