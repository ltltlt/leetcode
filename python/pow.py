'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Ubuntu
  > Author:		ty-l6
  > Mail:		liuty196888@gmail.com
  > File Name:		pow.py
  > Created Time:	2017-08-15 Tue 21:26
'''''''''''''''''''''''''''''''''''''''''''''''''''

# this problem is just like the divide problem.
# with one value to approach some value, our value approach another value with it

from math import sqrt
def mypow(x, n):
    if n == 0: return 1
    if n < 0:
        x = 1/x
        n = -n
    exponent = 1
    result = x
    if result < 0 and n%2:
        neg = True
    else: neg = False           # if neg information not keep, assume x<0 and n==3
                                # the result will be positive, since it is x^2, 
                                # because result_factor is calculate by result, it will also be positive
                                # which finally cause final result be positive, which is a mistake
    while exponent < n:
        exponent *= 2
        result *= result
    if exponent == n or result == 0:
        return result
    else:
        result = sqrt(result)
        exponent /= 2

        exponent_factor = exponent / 2
        result_factor = sqrt(result)
        
        # while exponent approach to n, make result approach to x^n
        while exponent != n:
            while exponent < n:
                exponent += exponent_factor
                result *= result_factor
            if exponent == n:
                if neg: return -result
                else: return result
            exponent -= exponent_factor
            result /= result_factor
            exponent_factor /= 2
            result_factor = sqrt(result_factor)

if __name__ == '__main__':
    import pprint
    pprint.pprint(mypow(*map(float, input().strip().split())))
