import math
class Solution:
    def myAtoi(self, str: str) -> int:
        digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        sign = 1
        sol = 0
        if len(str)==0:
            return 0
        for i in range(len(str)):
            if str[i] == ' ':
                continue
            elif str[i] == '+':
                i+=1
                break
            elif str[i] == '-':
                i+=1
                sign = -1
                break
            elif str[i] in digits.keys():
                break
            return 0
        for j in range(i,len(str)):
            if not str[j] in digits.keys():
                break
            sol = 10*sol + digits[str[j]]
        sol *= sign
        if sol > 2**31-1:
            return 2**31-1
        if sol < -2**31:
            return -2**31
        return sol

    def test_examples(self):
        print(self.myAtoi(self,'42'))
        print(self.myAtoi(self,'   -42'))
        print(self.myAtoi(self,'4193 with words'))
