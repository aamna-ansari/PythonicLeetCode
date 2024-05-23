class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        add = 0

        for i in range(len(stones)):
             if stones[i] in jewels: 
                add += 1
        return add  

#Solution:
jewels = "aA"
stones = "aAAbbbb"

solution = Solution()
count = solution.numJewelsInStones(jewels, stones)
print(count) 