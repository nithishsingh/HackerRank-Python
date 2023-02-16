# Problem: https://www.hackerrank.com/challenges/py-if-else/problem
# Score: 10

# General Solution 
def wierd(n):
    if n % 2 == 1 or 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird')


wierd(int(input()))


# Alternative Solution
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 == 1 or 6<= n <= 20:
        print("Weird")
    else:
        print("Not Weird")

# Alternative solution 02:

""" In more Readable Format of what is happing in the code. """

if n%2 != 0:
    print("Weird")
elif n%2 == 0 and n>2 and n<=5:
    print("Not Weird")
elif n%2 ==0 and n > 6 and n <=20:
    print("Weird")
else:
    print("Not Weird")

# Alternative Solution without if...elif...else....



if __name__ == '__main__':
    n = int(input().strip())
    print('Weird'*(n % 2 or (n % 2 == 0 and 6 <= n <= 20)) + 'Not Weird'*(n % 2 == 0 and (n > 20 or 2 <= n <= 5)))