'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Ubuntu
  > Author:		ty-l8
  > Mail:		liuty196888@gmail.com
  > File Name:		climbing_stairs.py
  > Created Time:	2017-08-20 Sun 00:17
'''''''''''''''''''''''''''''''''''''''''''''''''''

from functools import reduce
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in (0, 1, 2): return n
        ways = 0
        for _2nums in range(n//2+1):
            _1nums = n - 2*_2nums
            A = _2nums + _1nums
            ways += self.combination_num(A, _2nums)
        return int(ways)
    def combination_num(self, A, B):
        """
        calculate combination num B in A
        """
        if B == A: return 1
        if B in (A-1, 1): return A
        return reduce(lambda x, y:x*y, range(B+1, A+1)) // reduce(lambda x, y:x*y, range(2, A-B+1))
    
    def fast_combination_num(self, A, B):
        if B == A: return 1
        if B in (A-1, 1): return A
        result = A
        for i in range(0, A-B-1):
            result = result * (i+B+1) / (i+2)       # because it's precision is too low, when it come to 29, it will make mistake
        return int(result)
    def fast_combination_num(self, A, B):       # from 25% to 61%
        if B == A: return 1
        if B in (A-1, 1): return A
        result = A
        for i in range(B+1, A): result *= i
        for i in range(2, A-B+1): result /= i
        return result
    def faster(self, n):
        """
        from 5% to 25%
        """
        if n in (0, 1, 2): return n
        return reduce(lambda x,y:x+y, (self.combination_num(n-_2nums, _2nums) for _2nums in range(n//2+1)))
