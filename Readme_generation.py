import os



def get_folder_name(path):
    folders = []
    for item in os.listdir(path):
        if not os.path.isfile(item) and item not in ('.git'):
            folders.append(item)
    return folders

def get_file_names(path):
    files = os.listdir(path)
    return files

def get_url_scores(path):
    infile = open(path, 'r', encoding='utf-8')
    url = infile.readline().split()[-1]
    score = infile.readline().split()[-1]
    infile.close()
    return url,score

def get_total_probelm():
    all = 0
    folders = get_folder_name(os.getcwd())
    for folder in folders:
        subfolders  = get_folder_name(os.path.join(os.getcwd(),folder))
        for subfolder in subfolders:
            all += len(get_file_names(os.path.join(os.getcwd(),folder,subfolder)))
            return all

readmefile = open('README.md', 'w', encoding = 'utf-8')

print('<p align="center"><a href="https://www.hackerrank.com/nithishsingh"><img src="https://i0.wp.com/gradsingames.com/wp-content/uploads/2016/05/856771_668224053197841_1943699009_o.png" ></a></p>', file=readmefile)
print(file=readmefile)
print('# Solutions to Hackerrank python problems', file=readmefile)
print('# Only For Educational Purpose use it as Reference not a point of solution', file=readmefile)
print('This repository contains ' + str(get_total_probelm()) + ' solutions to Hackerrank practice problems with Python 3', file=readmefile)
print(file=readmefile)
print('Updated daily :) If it was helpful please press a star.', file=readmefile)
print(file=readmefile)
print('[![GitHub last commit](https://img.shields.io/github/last-commit/nithishsingh/HackerrankPractice.svg)](https://github.com/nithishsingh/HackerRank-Python) ', file=readmefile)
print('[![GitHub commit activity the past week, 4 weeks, year](https://img.shields.io/github/commit-activity/y/nithishsingh/HackerrankPractice.svg)](https://github.com/nithishsingh/HackerRank-Python)', file=readmefile)
print('[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/nithishsingh/HackerrankPractice.svg)](https://github.com/nithishsingh/HackerRank-Python) ', file=readmefile)
print('[![GitHub stars](https://img.shields.io/github/stars/nithishsingh/HackerrankPractice.svg)](https://github.com/nithishsingh/HackerRank-Python)', file=readmefile)
print(file=readmefile)

folders = get_folder_name(os.getcwd())
for folder in sorted(folders):
    print('- ' + folder, file=readmefile)
    subfolders = get_folder_name(os.path.join(os.getcwd(), folder))
    for subfolder in sorted(subfolders):
        print('    ' + subfolder, file=readmefile)
        files = get_file_names(os.path.join(os.getcwd(), folder, subfolder))
        for file in sorted(files):
            if file.endswith(('.py')):
                url, score = get_url_scores(os.path.join(os.getcwd(), folder, subfolder, file))
                print('        - ' + "".join(file.split(".")[1:-1])[1:]
                      + ' | [Problem](' + url
                      + ')'
                      + ' | [Solution]'
                      + '(https://github.com/nithishsingh/HackerRank-Python/:blob/master/'
                      + folder.replace(' ', '%20') + '/' + subfolder.replace(' ', '%20') + '/'
                      + file.replace(' ', '%20') + ')'
                      + ' | Score: ' + str(score), file=readmefile)

readmefile.close()
