# Problem: https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem
# Score: 100

def miniMaxSum(arr):
    arr= sorted(arr)
    print(sum(arr[:4]), sum(arr[-4:]))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)