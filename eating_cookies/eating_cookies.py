#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
  divide_by_3 = 0
  divide_by_2 = 0
  divide_by_1 = 0

 if n < 2:
     return 1
 elif n == 1:
     return 2
 elif n == 3:
     return 4
 elif n == 4:
     return 5
    # eat 1 cookie 4 times
    # eat 1 then eat 3
    # eat 2 then 2
    # eat 1 then 4
    # eat 4

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
