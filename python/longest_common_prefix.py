'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Ubuntu
  > Author:		ty-l6
  > Mail:		liuty196888@gmail.com
  > File Name:		longest_common_prefix.py
  > Created Time:	2017-08-15 Tue 22:13
'''''''''''''''''''''''''''''''''''''''''''''''''''

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        col_len = min(len(str) for str in strs)

        result = 0
        for i in range(col_len):
            if 1 != len(set(s[i] for s in strs)):
                return strs[0][:result]
            else: result += 1
        return strs[0][:result]

if __name__ == '__main__':
    solution = Solution()
    import pprint
    pprint.pprint(solution.longestCommonPrefix(['a']))
