"""Brute Force Approach to Count Digits in an Integer.
Time Complexity: O(log10N + 1),
Space Complexity : O(1)
"""

# def countDigits(n):
#     cnt = 0
#     while n > 0:
#         cnt = cnt + 1
#         n = n // 10
#     return cnt

"""Efficient Approach to Count Digits in an Integer using Logarithm.
Time Complexity: O(1),
Space Complexity : O(1)"""

import math

def countDigits(n):
    cnt = int(math.log10(n) + 1)
    return cnt

N = 329823
print("N:", N)
digits = countDigits(N)
print("Number of Digits in N:", digits)
                                