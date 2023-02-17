# Problem: https://www.hackerrank.com/challenges/python-print/problem
# Score: 20


for i in range(1, int(input()) + 1):
    print(i, end='')

# Alternative Solution 01

if __name__ == '__main__':
    n = int(input())
    
    for i in range(1,n+1):
        print(i, end="")