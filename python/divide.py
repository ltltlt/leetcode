'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Ubuntu
  > Author:		ty-l6
  > Mail:		liuty196888@gmail.com
  > File Name:		divide.py
  > Created Time:	2017-08-15 Tue 17:23
'''''''''''''''''''''''''''''''''''''''''''''''''''

def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    if divisor == 0: return 0
    neg = (dividend > 0) ^ (divisor > 0)

    dividend = dividend if dividend>=0 else -dividend
    divisor = divisor if divisor>=0 else -divisor

    # binary search
    #　first: get divisor*2^k, which divisor*2^k>=dividend while divisor*2^(k-1)<dividend
    result = 1                      # value to approach our result
    approximate_value = divisor     # value to approach dividend
    while approximate_value<dividend:
        approximate_value += approximate_value
        result += result
    # second: use divisor*2^(k-1) to approach dividend
    if approximate_value > dividend:
        approximate_value >>= 1
        result >>= 1
        approximate_factor = approximate_value >> 1
        result_factor = result >> 1
        # approach closely
        while approximate_factor > 0 and result_factor > 0: # when approximate_value approach to dividend, result will approach to true value
            while approximate_value < dividend:
                approximate_value += approximate_factor
                result += result_factor
            if approximate_value == dividend:
                break
            approximate_value -= approximate_factor
            result -= result_factor
            approximate_factor >>= 1
            result_factor >>= 1

    if neg:
        result = -result
    result = result if result<=2147483647 else 2147483647
    result = result if result>=-2147483648 else -2147483648
    return result

if __name__ == '__main__':
    print(devide(*map(int, input().strip().split())))
