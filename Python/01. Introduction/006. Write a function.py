# Problem: https://www.hackerrank.com/challenges/write-a-function/problem
# Score: 10


def is_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

year = int(input())
print(is_leap(year))

# Alternative Solution 01

def is_leap(year):
    
    if (year % 400 == 0) and (year % 100 == 0):
         return True

    elif (year % 4 ==0) and (year % 100 != 0):
        return True

    else:
        return False
year = int(input())
print(is_leap(year))