# Problem: https://www.hackerrank.com/challenges/swap-case/problem
# Score: 10


def swap_case(s):
    return s.swapcase() # Inbuilt Function


# Alternative Solution 01

def swap_case(s):
    return "".join([x.lower() if x.isupper() else x.upper() for x in s])  # with List Comperhension


# Alternative Solution 02
def swap_case(s):
    word = [letter.lower() if letter.isupper() else 
            letter.upper() if letter.islower() else letter
            for letter in s]
    return ''.join(word)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)