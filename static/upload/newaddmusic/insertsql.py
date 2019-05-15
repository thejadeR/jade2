import pymysql
import os
con = pymysql.connect(user='root',password='123456',host='localhost',port=3306,database='jadedb',charset='utf8')

cursor = con.cursor()

music_list = os.listdir(os.path.dirname(__file__))
# print(music_list)

for music in music_list:
    if music.endswith('.mp3'):
        music_title = music[:music.rfind('.')]

        # print(music_title)
        # print(music)
        num_size = round(os.path.getsize(music) / 1024 / 1024, 2)
        file_size = f'{num_size}M'

        sql = 'insert into myweb_music(title,thesrc,file_size) value ("%s","%s","%s")'%(music_title,music,file_size)

        cursor.execute(sql)

con.commit()

cursor.close()
con.close()