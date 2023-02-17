# Problem: https://www.hackerrank.com/challenges/nested-list/problem
# Score: 10


if __name__ == '__main__':
    
    marksheet=[]  # collecting Name and score in list
    scorelist =[] # collecting score alone in the list

    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet += [[name,score]]  # appending to the list
        scorelist += [score]    # appending to the list
        
    b = sorted(list(set(scorelist)))[1]  # sorting the uniqe value in the list due to fun set
    
    for n,s in sorted(marksheet):  # using sorted marksheet name will be asce order
        if s==b: # comparing lower score again the score (original list)
            print(n)




# alternative Solution 01

def secondLowestGrade(classList):
    secondLowestScore = sorted(set(_[1] for _ in classList))[1]
    result = sorted([_[0] for _ in classList if _[1] == secondLowestScore])
    return result


numberOfStudents = int(input())
classList = []
for i in range(numberOfStudents):
    classList.append([str(input()), float(input())])
print('\n'.join(secondLowestGrade(classList)))
