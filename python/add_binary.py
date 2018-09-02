'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Ubuntu
  > Author:		ty-l8
  > Mail:		liuty196888@gmail.com
  > File Name:		add_binary.py
  > Created Time:	2017-08-20 Sun 00:05
'''''''''''''''''''''''''''''''''''''''''''''''''''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return self.convert_back(self.convert(a) + self.convert(b))
    def convert(self, binary):
        """
        :type binary: str
        :rtype: int
        """
        result = 0
        for c in binary:
            result = result*2+(1 if c=='1' else 0)
        return result
    def convert_back(self, value):
        """
        :type value: int
        :rtype: str
        """
        if value == 0: return '0'
        bits = []
        while value:
            bits.append(str(value % 2))
            value //= 2
        return ''.join(bits[::-1])
