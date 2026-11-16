class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}
        for k in strs:
            key=tuple(sorted(k))
            if key not in hash:
                hash[key]=list()
                hash[key].append(k)
            elif key in hash:
                hash[key].append(k)

        output=[hash[key] for key  in hash]
        return output