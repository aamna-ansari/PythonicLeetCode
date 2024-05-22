from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            number2 = target -nums[i]
            if number2 in hashMap:
                 return [hashMap[number2],i]
            else:
                 hashMap[nums[i]] = i   

# solution 
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result)