class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=nums+nums
        return ans

a= Solution()
print(a.getConcatenation([1,2,3,4]))