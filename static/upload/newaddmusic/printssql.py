import os

# music_list = os.listdir(os.path.dirname(__file__))
# # print(music_list)
#
# for music in music_list:
#     if music.endswith('.mp3'):
#         music_title = music[:music.rfind('.')]
#         # print(music)
#         # print(os.path.getsize('Taylor Swift - Love Story.mp3'))
#         # print(music_title)
#         num_size = round(os.path.getsize(music) / 1024 / 1024, 2)
#         file_size = f'{num_size}M'
#         # print(file_size)
#         # print(music)
#         sql = 'insert into myweb_music(title,thesrc,file_size) value ("%s","%s","%s")' % (music_title, music, file_size)
#         print(sql)

str1 = 'adaf.mp3'

if str1.endswith('.mp3'):
    print('affa')