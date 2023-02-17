# Problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Score: 10


n = int(input())
arr = list(map(int, input().split()))
print(max([x for x in arr if x != max(arr)]))

# Alternative Solution 01

if __name__ == '__main__':
    n = int(input())
    arr =list(map(int, input().split()))
    m=max(arr)
    while max(arr) == m:
        arr.remove(max(arr))
    print(max(arr))