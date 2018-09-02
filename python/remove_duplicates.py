'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Ubuntu
  > Author:		ty-l6
  > Mail:		liuty196888@gmail.com
  > File Name:		remove_duplicates.py
  > Created Time:	2017-08-15 Tue 21:15
'''''''''''''''''''''''''''''''''''''''''''''''''''

def removeDuplicates(nums):
    length = len(nums)
    
    index = 0
    while index < length-1:
        while index < length-1 and nums[index] == nums[index+1]:
            length -= 1
            nums.pop(index+1)
        index += 1
    return length

if __name__ == '__main__':
    import pprint
    l = list(map(int, input().strip().split()))
    pprint.pprint(removeDuplicates(l))
    pprint.pprint(l)
