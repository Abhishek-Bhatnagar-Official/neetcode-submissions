class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable={nums[0]:0}
        for i in range(1,len(nums)):
            d=target-nums[i]
            if d in hashtable:
                return [hashtable[d],i]
            else:
                hashtable[nums[i]]=i