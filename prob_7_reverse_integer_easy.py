import math
def reverse(x: int) -> int:
    sign = 2*int(x>0)-1
    x = str(abs(x))
    ans =  sign*int(''.join([x[i] for i in range(len(x)-1,-1,-1)]))
    if ans < -2**31 or ans > 2**31-1:
        return 0
    else:
        return ans
