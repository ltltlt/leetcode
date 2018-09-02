'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Ubuntu
  > Author:		ty-l6
  > Mail:		liuty196888@gmail.com
  > File Name:		reverse_integer.py
  > Created Time:	2017-08-15 Tue 16:03
'''''''''''''''''''''''''''''''''''''''''''''''''''

def reverse(x):
    result = 0
    x = str(x)
    if x[0] == '-':
        neg = True
        x = x[1:]
    else: neg = False
    for c in x[::-1]:
        result *= 10
        result += int(c)
    if neg: result = -result
    if not (-4294967296/2 < result < 4294967294/2):
        return 0
    return result
if __name__ == '__main__':
    print(reverse(int(input().strip())))
