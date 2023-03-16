# Problem: https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem
# Score: 100


def plusMinus(arr):
    pv = 0
    nv = 0
    z = 0
    ln = len(arr) # length of arr
    for i in (arr):
        if i>0:
            pv+=1  # pv is positive value
        elif i<0:
            nv+=1  # nv is negative Value
        else:
            z+=1   # z is zeros
    
    print(pv/ln)
    print(nv/ln)
    print(z/ln)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
