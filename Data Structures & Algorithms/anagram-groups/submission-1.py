class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}
        for i in range(len(strs)):
            if tuple(sorted(strs[i])) not in hash:
                hash[tuple(sorted(strs[i]))]=list()
                hash[tuple(sorted(strs[i]))].append(strs[i])
            elif tuple(sorted(strs[i])) in hash:
                hash[tuple(sorted(strs[i]))].append(strs[i])

        output= list(hash[x] for x in hash)
        return output

a=Solution()
input=["act","pots","tops","cat","stop","hat"]
print(a.groupAnagrams(input))