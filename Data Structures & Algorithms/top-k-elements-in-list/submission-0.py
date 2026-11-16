class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            if num not in count:
                count[num]=1
            else:
                count[num]+=1
        
        buckets=[[] for i in range(len(nums)+1)]

        for num in count:
            buckets[count[num]].append(num)

        result=[]
        for i in range(len(nums),0,-1):
            num= buckets[i]
            for s in num:
                result.append(s)
                if len(result)==k:
                    return result