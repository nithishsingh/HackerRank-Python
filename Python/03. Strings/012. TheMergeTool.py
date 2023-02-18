# Problem:  https://www.hackerrank.com/challenges/merge-the-tools/problem
# Score: 40



def merge_the_tools(string, k):
    for x in range(len(string) // k):
        res = [] 
        for letter in string[x*k : x*k+k]:
            if letter not in res:
                res.append(letter) 
        print(''.join(res))
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# Alternative solution 01

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        # Use slicing to get the current substring
        substring = string[i:i+k]
        # Create a set of unique characters
        unique_chars = set(substring)
        # Use string method 'join' to join the unique characters and print the result
        print(''.join(unique_chars))


# Alternative Solution 02

from textwrap import wrap

def merge_the_tools(string, k):
    ls = wrap(string, k)
    for x in ls:
        result = x[0]
        for i in range(1,k): 
            if x[i] not in result:
                result += x[i]
            else: 
                continue
        print(result)
 
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)