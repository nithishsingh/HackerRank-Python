# Problem: https://www.hackerrank.com/challenges/python-string-split-and-join/problem
# Score: 10

#using split join

def split_and_join(line):
    return "-".join(line.split())

# using print

def split_and_join(line):
    print(*line.split(" "),sep="-")

# Alternaive Solution

print(input().replace(" ","-"))