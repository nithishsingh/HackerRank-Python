# Problem: https://www.hackerrank.com/challenges/python-loops/problem
# Score: 10


for i in range(int(input())):
    print(i ** 2)


# Alternative Solution 01

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i*i)