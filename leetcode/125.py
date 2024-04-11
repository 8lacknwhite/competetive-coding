import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        answer = True
        s = re.sub('[\W_]','',s)
        s = s.lower()
        if len(s) ==0 or len(s)== 1:
            return answer
        else:
            for i in range(len(s)):
                if s[i] == s[-(i+1)]:
                    answer = True
                else:
                    answer = False
                    break
        return answer
                