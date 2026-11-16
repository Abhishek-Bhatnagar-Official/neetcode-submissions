import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s= re.sub(r'[^\w]',"",s)
        rev= s[::-1]
        if s==rev:
            return True
        else:
            return False