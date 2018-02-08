import os

dir_path = 'E:\电影'

def change_movie_name(dir_path):
    os.chdir(dir_path)
    if os.path.exists(dir_path) :
        for root, dirs, files in os.walk(dir_path):
            print(root)  # 当前目录路径
            print(dirs)  # 当前路径下所有子目录
            print(files)  # 当前路径下所有非目录子文件
            for i in files:
                if i[0:19] == '[电影天堂www.dygod.com]':
                    print(i[20:])
                    os.rename(i,i[20:])
    else :
        print('该路径不存在')
change_movie_name(dir_path)
