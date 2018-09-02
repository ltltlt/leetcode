'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Ubuntu
  > Author:		ty-l6
  > Mail:		liuty196888@gmail.com
  > File Name:		atoi.py
  > Created Time:	2017-08-15 Tue 16:17
'''''''''''''''''''''''''''''''''''''''''''''''''''

def myatoi(string):
    string = string.strip()
    if not string: return 0

    neg = False
    if string[0] in ('-', '+'):
        if string[0] == '-':
            neg = True
        string = string[1:]
    result = 0
    try:
        for s in string:
            v = int(s)
            result *= 10
            result += v
    except Exception:
        pass
    if neg:
        result = -result
    result = result if result<2147483647 else 2147483647
    result = result if result>-2147483648 else -2147483648
    return result

if __name__ == '__main__':
    print(myatoi(input().strip()))
