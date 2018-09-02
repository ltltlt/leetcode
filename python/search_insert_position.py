'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Ubuntu
  > Author:		ty-l6
  > Mail:		liuty196888@gmail.com
  > File Name:		search_insert_position.py
  > Created Time:	2017-08-15 Tue 22:20
'''''''''''''''''''''''''''''''''''''''''''''''''''

def searchInsert(nums, target):
    l, u = 0, len(nums)-1
    while l<u:
        m = (u+l)//2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            u = m-1
        else: l = m+1
    if nums[l] < target:
        return l+1
    return l

if __name__ == '__main__':
    print(searchInsert([1, 3], 2))
