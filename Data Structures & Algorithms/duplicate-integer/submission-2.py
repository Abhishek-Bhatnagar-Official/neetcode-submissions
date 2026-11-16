class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        flag=0
        for i in nums:
            if i in hashset:
                flag=1
                break
            else:
                hashset.add(i)
        if flag==1:
            return True
        else:
            return False

a= Solution()
nums = [1, 2, 3, 3]
print(a.hasDuplicate(nums))