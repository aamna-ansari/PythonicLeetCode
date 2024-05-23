
class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        str = ''
        for i in x:
            str +=i[::-1] + ' '
        return str.rstrip()
    
    
  #solution  
solution = Solution()
result = solution.reverseWords("Let's take LeetCode contest")
print(result)
