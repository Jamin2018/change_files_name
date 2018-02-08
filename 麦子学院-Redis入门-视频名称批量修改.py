import requests
from bs4 import BeautifulSoup
import os


url = 'http://www.maiziedu.com/course/337/'
dir_path = 'E:\迅雷下载\麦子学院-Redis入门'

def mp4_title(url):
    html = requests.get(url)
    Soup = BeautifulSoup(html.content,'html.parser')
    all_li = Soup.find('ul',class_='lesson-lists').findAll('li')
    titles = []
    n = 0
    for i in all_li:
        n +=1
        titles.append(i.find('span',class_='fl').text)
    return titles

def change_files_name(dir_path,url):
    os.chdir(dir_path)   # 移动到该目录下
    titles = mp4_title(url)
    n = 0
    for title in titles:
        n += 1
        os.rename('redisrm'+str(n)+'.mp4',title+'.mp4')
change_files_name(dir_path,url)
