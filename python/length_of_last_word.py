'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Ubuntu
  > Author:		ty-l6
  > Mail:		liuty196888@gmail.com
  > File Name:		length_of_last_word.py
  > Created Time:	2017-08-18 Fri 00:28
'''''''''''''''''''''''''''''''''''''''''''''''''''

def lengthOfLastWord(s):
    s = s.strip()
    if not s: return 0

    length = 0
    for c in s:
        if c == ' ':
            length = 0
        else:
            length += 1
    return length
