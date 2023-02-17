# Problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Score: 10


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    
    avg_score = sum (student_marks[query_name]) / len(student_marks[query_name])
    print(f"{avg_score:.2f}")



# Alternative solution 01

def readScores(listOfStudents):
    line = list(input().split())
    avScore = sum(map(float, line[1:])) / 3
    name = line[0]
    listOfStudents[name] = avScore


n = int(input())
listOfStudents = dict()
for i in range(n):
    readScores(listOfStudents)
print('%.2f' % listOfStudents[input()])
