import math
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return s
        sol = s[0]
        for i in range(1,len(s)):
            j = 1
            while j < min(i+1,len(s)-i) and s[i-j] == s[i+j]: #Test for palindrome of odd length starting with middle point s[i]
                j+=1
            if 2*(j-1)+1 > len(sol):
                sol = s[i-j+1:i+j]
            j=0
            while j < min(i,len(s)-i) and s[i-j-1] == s[i+j]: #Test for palindrom of even length with middle point between s[i] and s[i-1]
                j+=1
            if 2*j > len(sol):
                sol = s[i-j:i+j]
        return sol

    def test_examples(self):
        print(self.longestPalindrome(self,'babad'))
        print(self.longestPalindrome(self,'cbbd'))
