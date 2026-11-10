class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashS, hashT= {},{}
        flag=0
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

        for key in hashT:
            if key not in hashS or hashS[key]!=hashT[key]:
                flag+=1
        
        if flag==0:
            return True
        else:
            return False