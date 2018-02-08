import requests
from bs4 import BeautifulSoup
import os


url = 'http://www.maiziedu.com/course/306/'
dir_path = 'E:\迅雷下载\麦子学院-Mysql基础'

def mp4_title(url):
    '''
    获取该视频网站的视频标题
    '''
    html = requests.get(url)
    Soup = BeautifulSoup(html.content,'html.parser')
    all_li = Soup.find('ul',class_='lesson-lists').findAll('li')
    titles = []
    n = 0
    for i in all_li:
        n +=1
        if n < 10:
            titles.append(i.find('span',class_='fl').text[0:-4])
        else:
            titles.append(i.find('span', class_='fl').text[0:-5])
    return titles

def change_files_name(dir_path,url):
    '''
    根据该url获得的视频标题，进行对应的修改
    '''
    os.chdir(dir_path)   # 移动到该目录下
    titles = mp4_title(url)
    n = 0
    for title in titles:
        n += 1
        os.rename('mysql_basic_'+str(n)+'.mp4',title+'.mp4')
change_files_name(dir_path,url)