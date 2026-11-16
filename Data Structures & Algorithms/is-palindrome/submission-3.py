import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s= re.sub(r'[^\w]',"",s)
        flag=0
        right= len(s)-1
        left= 0
        while right>left:
            if s[left]!=s[right]:
                return False
                break
            
            right-=1
            left+=1
        return True