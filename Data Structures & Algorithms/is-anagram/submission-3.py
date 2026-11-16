class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        flag=0
        hashS,hashT={},{}

        for k in s:
            if k not in hashS:
                hashS[k]=1
            else:
                hashS[k]+=1
        for k in t:
            if k not in hashT:
                hashT[k]=1
            else:
                hashT[k]+=1

        for i in hashT:
            if i not in hashS or hashS[i]!=hashT[i]:
                flag=1
                break
        if flag==0:
            return True
        else:
            return False