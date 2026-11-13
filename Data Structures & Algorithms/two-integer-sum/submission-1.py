class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked={nums[0]:0}
        for i in range(1,len(nums)):
            c=target-nums[i]
            if c in checked:
                return [checked[c],i]
            else:
                checked[nums[i]]=i





a=Solution()
sequence=[3,4,5,6]
target=7
print(a.twoSum(sequence,target))