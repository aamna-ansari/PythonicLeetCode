# Method #1:
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)
    
# Method #2:

from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = set(nums1)
        num2 = set(nums2)
        arr = []
        for i in num1:
            if i in num2:
                arr.append(i)
        return arr
    
#solution
solution = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = solution.intersection(nums1, nums2)
print(result) 