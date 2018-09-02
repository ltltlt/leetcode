'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Ubuntu
  > Author:		ty-l6
  > Mail:		liuty196888@gmail.com
  > File Name:		isPalindrome.py
  > Created Time:	2017-08-15 Tue 17:04
'''''''''''''''''''''''''''''''''''''''''''''''''''

def isPalindrome(x):
    if (x!=0 and x%10 == 0) or x<0:
        return False
    sum = 0
    while sum < x:
        sum = sum*10 + x%10
        x /= 10
    return sum == x or sum/10 == x
