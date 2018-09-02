'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Ubuntu
  > Author:		ty-l6
  > Mail:		liuty196888@gmail.com
  > File Name:		valid_parentheses.py
  > Created Time:	2017-08-17 Thu 23:27
'''''''''''''''''''''''''''''''''''''''''''''''''''

def isValid(s):
    '''
    :type s: str
    :rtype: bool
    '''
    stack = []
    d = { ')':'(', ']':'[', '}':'{' }
    for c in s:
        if c in '{([':
            stack.append(c)
        else:
            if not stack or stack.pop() != d[c]:
                return False
    return not stack
