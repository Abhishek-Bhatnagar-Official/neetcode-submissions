class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right= len(numbers)-1
        left=0
        while right>left:
            val=numbers[right]+numbers[left]
            if val > target:
                right-=1
            elif val<target:
                left+=1
            elif val==target:
                return [left+1,right+1]