import os
import functools


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

readmefile = open('Readme.md', 'w', encoding = 'utf-8')

print('<p align = "center"><a href = "https://www.hackerrank.com/nithishsingh" ')