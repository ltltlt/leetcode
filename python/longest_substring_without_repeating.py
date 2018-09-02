'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Ubuntu
  > Author:		ty-l6
  > Mail:		liuty196888@gmail.com
  > File Name:		longest_substring_without_repeating.py
  > Created Time:	2017-08-17 Thu 22:08
'''''''''''''''''''''''''''''''''''''''''''''''''''

def lengthOfLongestSubstring(s):
    '''
    :type s: str
    :rtype: int
    '''
    max_len = 0
    s_len = len(s)
    for i in range(s_len):
        d = set()
        length = 0
        for end in s[i:]:
            if end not in d:
                d.add(end)
                length += 1
            else:
                break
        max_len = max(max_len, length)
    return max_len

if __name__ == '__main__':
    import pprint
    # pprint.pprint(lengthOfLongestSubstring(input().strip()))

def better_solution(s):
    max_len = 0
    s_len = len(s)
    i = 0
    while i < s_len - max_len:
        d = set()
        for end in s[i:]:
            if end not in d:
                d.add(end)
            else: break
        max_len = max(max_len, len(d))
        i += 1
    return max_len

if __name__ == '__main__':
    import pprint
    # pprint.pprint(better_solution(input().strip()))

# dynamic programming
def best_solution(s):
    s_len = len(s)
    max_len = left = right = 0
    d = set()
    while right < s_len:
        if s[right] not in d:
            d.add(s[right])
            right += 1
            max_len = max(max_len, right-left)
        else:
            d.remove(s[left])
            left += 1
    return max_len

if __name__ == '__main__':
    import pprint
    pprint.pprint(best_solution(input().strip()))

# optimize
def best_solution(s):
    s_len = len(s)
    max_len = left = right = length = 0
    d = set()
    length = right - left
    while right < s_len:
        if s[right] not in d:
            d.add(s[right])
            right += 1
            length += 1
            max_len = max_len if max_len >= length else length
        else:
            d.remove(s[left])
            left += 1
            length -= 1
    return max_len
if __name__ == '__main__':
    import pprint
    # pprint.pprint(best_solution(input().strip()))
