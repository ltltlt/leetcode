'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Ubuntu
  > Author:		ty-l6
  > Mail:		liuty196888@gmail.com
  > File Name:		3sum.py
  > Created Time:	2017-08-15 Tue 19:52
'''''''''''''''''''''''''''''''''''''''''''''''''''

# more details, see: https://www.sigmainfy.com/blog/summary-of-ksum-problems.html
# time complexity O(nlogn+n^2)

# two sum: one point forward, one backword, linear time complexity
def treeSum(nums):
    result_list = set()
    nums.sort()
    for i, num in enumerate(nums):
        target = -num                       # lock one, then use two-sum to focus other two
        j, k = 0, len(nums)-1
        while j < k:
            if j == i:
                j += 1
            elif k == i:
                k -= 1
            else:
                value = nums[j] + nums[k]
                if value == target:
                    if i > j:
                        if k > i:
                            result_list.add((nums[j], num, nums[k]))
                        else: result_list.add((nums[j], nums[k], num))
                    else:
                        if k > i:
                            result_list.add((num, nums[j], nums[k]))
                    j, k = j+1, k-1
                elif value < target:
                    j += 1
                else: k -= 1
    return list(result_list)

if __name__ == '__main__':
    import pprint
    pprint.pprint(treeSum(list(map(int, input().strip().split()))))
