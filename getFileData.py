import pandas as pd
from agithub.GitHub import GitHub
import os
import sys
from bs4 import BeautifulSoup

def get_code_snippets(body):
    soup = BeautifulSoup(body, 'html.parser')
    snippets = []
    for snippet in soup.find_all('code'):
        snippets.append(snippet.get_text())
    return snippets

def get_file_data(index, request_counter):
    dir_name = sub_data['RepoName'][index]
    if not(os.path.isdir(dir_name)):
        os.mkdir(dir_name)
    url = sub_data['GHUrl'][index]
    url = url.split('/')[3:]
    owner, repo = url[0], url[1]
    fpath = '/'.join(url[3:])
    dir_name = os.path.join(dir_name,fpath.replace('/','-').replace('.java',''))
    if not(os.path.isdir(dir_name)):
        os.mkdir(dir_name)
    fname = fpath.split('/')[-1]
    if (LIMIT-request_counter-1)<0:
        print(f'Stopped at index = {index}')
        return request_counter
    commit_cmd = 'g.repos[owner][repo].commits.get(path=\''+fpath+'\')'
    commits = eval(commit_cmd)
    request_counter += 1
    if(LIMIT-request_counter-len(commits[1])<0):
        print(f'Stopped at index = {index}')
        return request_counter
    if len(commits[1]) < 4:
        print(f'Repo had less than 4 commits: {repo}')
        return request_counter
    # print(commits)
    ind = 1
    for commit in commits[1]:
        commit = commit['sha']
        file_cmd = 'g.repos[owner][repo].contents[fpath].get(headers=header,ref=\''+commit+'\')'
        f_dt_bytes = eval(file_cmd)
        request_counter+=1
        di = ''
        di = os.path.join(dir_name,str(ind))
        ind += 1
        if not(os.path.isdir(di)):
            os.mkdir(di)
        fullpath = os.path.join(di,fname)
        # print(type(f_dt_bytes[1]))
        # print(f_dt_bytes)
        if (type(f_dt_bytes[1])!=bytes):
            print(f'File content response not in bytes for {fullpath}')
            return request_counter
        open(fullpath,'wb').write(f_dt_bytes[1])
    snippets = get_code_snippets(sub_data['Body'][index])
    with open(dir_name+'/snippets.java', 'w') as f:
        for item in snippets:
            f.write("%s\n" % item)
            f.write("---------------------------------\n")
    print(f'Done for {repo}:{fullpath}')
    return request_counter




request_counter=0
table = pd.read_csv('table.csv')
g = GitHub('usrnm','passwd')
LIMIT=int(g.rate_limit.get()[1]['resources']['core']['remaining'])
print(f'Limit: {LIMIT}')

sub_data = table[['GHUrl','RepoName','Body']]
header = {'Accept': 'application/vnd.github.VERSION.raw'}
for i in range(5285, 5764):
    request_counter = get_file_data(i, request_counter)
    print(request_counter)
    if (request_counter>=LIMIT):
        break
# get_file_data(621,request_counter)
k = g.rate_limit.get()[1]['resources']['core']['remaining']
print(f'Remaining:{k}')

k=os.listdir('.')
for dd in k:
    if not(os.path.isdir(dd)) or dd.startswith('.'):
        continue
    print(f'parent:{dd}')
    k1 = os.listdir(dd)
    for k2 in k1:
        print(f'child:{k2}')
        act = os.listdir(os.path.join(dd,k2))
        if len(act)==0:
            os.rmdir(os.path.join(dd,k2))
            print(f'removing empty child:{k2}')
    k1 = os.listdir(dd)
    if len(k1)==0:
        os.rmdir(dd)
        print(f'removing parent:{dd}')