import os


def getFoldersNames(path):
    folders = []
    for item in os.listdir(path):
        if not os.path.isfile(item) and item not in ('.git', '.idea'):
            folders.append(item)
    return folders


def getFilesNames(path):
    files = os.listdir(path)
    return files


def getProblemURLandScore(path):
    inFile = open(path, 'r', encoding='utf-8')
    url = inFile.readline().split()[-1]
    score = inFile.readline().split()[-1]
    inFile.close()
    return url, score


def getTotalNumberOfProblems():
    totalNumber = 0
    folders = getFoldersNames(os.getcwd())
    for folder in folders:
        subfolders = getFoldersNames(os.path.join(os.getcwd(), folder))
        for subfolder in subfolders:
            totalNumber += len(getFilesNames(os.path.join(os.getcwd(), folder, subfolder)))
    return totalNumber


readmeFile = open('Documentation.md', 'w', encoding='utf-8')
print('<p align="center"><a href="https://www.hackerrank.com/nithishsingh"><img src="asset/png/Solution.png" ></a></p>', file=readmeFile)
print(file=readmeFile)
print('# HackerRank', file=readmeFile)
print('HackerRank Solution to Practice Problem in Various Domain.', file=readmeFile)
print(file=readmeFile)
print('# Only For Educational Purpose use it as Reference not a point of solution',file=readmeFile)
print(file=readmeFile)
print('This repository contains ' + str(getTotalNumberOfProblems()) + ' solutions to Hackerrank practice problems with Python 3.', file=readmeFile)
print(file=readmeFile)
print('Updated daily :) If it was helpful please press a star.', file=readmeFile)
print(file=readmeFile)
print('[![GitHub last commit](https://img.shields.io/github/last-commit/nithishsingh/HackerRank-Solution)](https://github.com/nithishsingh/HackerRank-Solution) ', file=readmeFile)
print('[![GitHub commit activity the past week, 4 weeks, year](https://img.shields.io/github/commit-activity/w/nithishsingh/Hackerrank-Solution)](https://github.com/nithishsingh/HackerRank-Solution)', file=readmeFile)
print('[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/nithishsingh/HackerRank-Solution)](https://github.com/nithishsingh/HackerRank-Solution) ', file=readmeFile)
print('[![GitHub stars](https://img.shields.io/github/stars/nithishsingh/HackerRank-Solution)](https://github.com/nithishsingh/HackerRank-Solution)', file=readmeFile)
print(file=readmeFile)

folders = getFoldersNames(os.getcwd())
for folder in sorted(folders):
    print('- ' + folder, file=readmeFile)
    subfolders = getFoldersNames(os.path.join(os.getcwd(), folder))
    for subfolder in sorted(subfolders):
        print('    ' + subfolder, file=readmeFile)
        files = getFilesNames(os.path.join(os.getcwd(), folder, subfolder))
        for file in sorted(files):
            if file.endswith(('.py', '.sql')):
                url, score = getProblemURLandScore(os.path.join(os.getcwd(), folder, subfolder, file))
                print('        - ' + "".join(file.split(".")[1:-1])[1:]
                      + ' | [Problem](' + url
                      + ')'
                      + ' | [Solution]'
                      + '(https://github.com/nithishsingh/HackerRank-Solution/blob/master/'
                      + folder.replace(' ', '%20') + '/' + subfolder.replace(' ', '%20') + '/'
                      + file.replace(' ', '%20') + ')'
                      + ' | Score: ' + str(score), file=readmeFile)

readmeFile.close()