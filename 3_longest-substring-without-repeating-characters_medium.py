class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = start = 0
        for i in range(len(s)):
            if not s[i] in list(s[start:i]):
                print('going in')
                if i-start+1 > res:
                    print('further')
                    res = i-start+1
            else:
                start = start + s[start:i].index(s[i]) + 1
        return res

        
