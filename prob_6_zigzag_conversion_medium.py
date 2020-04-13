class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        sol = ''
        step1 = 2*(numRows-1)
        step2 = step1
        print(step1)
        for i in range(numRows):
            print(i,step2)

            j = 0
            while True:
                try:
                    sol += s[i + j*step1]
                except IndexError:
                    break
                try:
                    if not i in [0, numRows-1] :
                        sol += s[i + j*step1 + step2]
                except IndexError:
                    break
                j+=1
            step2 -= 2
        return sol
