import os
import random
import time

from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from jade1.settings import MEDIA_ROOT
from .models import *

# Create your views here.

# 音乐栏
def index(request):


    musics = Music.objects.filter(~Q(title__contains="峡谷之音"))
    return render(request,'music.html',context={'musics':musics})


def sc_music(request):
    if request.method == 'POST':
        themusic = request.FILES.get('themusic')
        # print('themusic：',themusic)
        if themusic:
            # 音乐标题
            music_name = request.POST.get('music_name')

            # 如果没取音乐标题，就取文件名字为标题
            if not music_name:
                music_name = themusic.name
                # 如果文件格式不是mp3，则强行变成mp3
                # if  not music_name.endswith('.mp3'):
                music_name = themusic.name[:themusic.name.rfind('.')]
                # print(name)str(random.randrange(1,100)) + '-' + music_name
            # print(music_name)

            # 文件名字f'{num_size}.mp3'
            filename = "%s.mp3"%(music_name)
            # 文件路径
            thepath = os.path.join(MEDIA_ROOT,'upload/index/{}'.format(filename))
            # 如果有同名文件，则直接返回，不保存
            if os.path.exists(thepath):
                return HttpResponse('已经有同名歌曲，请修改文件名')

            with open(thepath,'wb') as f1:
                for item in themusic.chunks():
                    f1.write(item)

                f1.flush()
            # 文件大小f'{num_size}M'
            num_size = round(os.path.getsize(thepath) / 1024 / 1024, 2)
            file_size = "%sM"%(num_size)

            musics = Music()
            musics.title = music_name
            musics.thesrc = filename
            musics.file_size = file_size
            musics.save()
            return redirect('jade:index')


        return redirect('jade:index')

    return redirect('jade:index')


def del_music(request):
    dz_id = request.GET.get('dz_id',None)

    if dz_id:
        musics = Music.objects.get(id=dz_id)
        if musics:
            thepath = os.path.join(MEDIA_ROOT, 'upload/index/{}'.format(musics.thesrc))
            # print(thepath)
            if os.path.exists(thepath):
                os.remove(thepath)
            musics.delete()

            return JsonResponse({'msg': '1'})
        # 音乐已经被删掉了
        else:
            return JsonResponse({'msg': '0'})

    return JsonResponse({'msg': '0'})




# 段子藍
def duanzi(request):
    duanzis = Duanzi.objects.all()


    return render(request,'duanzi.html',context={'duanzis':duanzis})


def sc_duanzi(request):

    # duanzi = request.GET.get('duanzi',None)
    duanzi = request.GET.get('duanzi',None)

    if duanzi:
        duanzis = Duanzi()
        duanzis.duanzi_context = duanzi
        duanzis.save()

        return redirect('jade:duanzi')

    return redirect('jade:duanzi')



def del_duanzi(request):
    dz_id = request.GET.get('dz_id',None)

    # print(dz_id,type(dz_id))
    if dz_id:
        # print('jinru')
        duanzi = Duanzi.objects.get(id=int(dz_id))
        duanzi.delete()

        return JsonResponse({'msg':'1'})

    return JsonResponse({'msg': '0'})





# 圖片藍
def tupian(request):
    tupians = Tupian.objects.all()


    return render(request,'tupian.html',context={'tupians':tupians})

def sc_tupian(request):
    if request.method == 'POST':
        tupian = request.FILES.get('headimg')
        # print('t：',tupian)
        if tupian:
            img_title = request.POST.get('img_title','未命名')

            filename = str(random.randrange(1,10000)) + '-' + tupian.name
            # print(filename)
            # print(MEDIA_ROOT)
            # MEDIA_ROOT = MEDIA_ROOT.replace('\\','/')
            thepath = os.path.join(MEDIA_ROOT,'upload/imgDir/{}'.format(filename))
            with open(thepath,'wb') as f1:
                for item in tupian.chunks():
                    f1.write(item)

                f1.flush()

            tupians = Tupian()
            tupians.title = img_title
            tupians.imgsrc = filename
            tupians.save()
            return redirect('jade:tupian')


        return redirect('jade:tupian')

    return redirect('jade:tupian')






def del_tupian(request):
    dz_id = request.GET.get('dz_id')
    if dz_id:
        tupians = Tupian.objects.get(id=dz_id)
        if tupians:
            thepath = os.path.join(MEDIA_ROOT, 'upload/imgDir/{}'.format(tupians.imgsrc))
            # print(thepath)
            if os.path.exists(thepath):
                os.remove(thepath)
            tupians.delete()

            return JsonResponse({'msg': '1'})
        # 图片已经被删掉了
        else:
            return JsonResponse({'msg': '0'})

    return JsonResponse({'msg': '0'})





# 留言板藍
def liuyanban(request):
    liuyanbans = Liuyanban.objects.all()


    return render(request,'liuyanban.html',context={'liuyanbans':liuyanbans})


def sc_liuyanban(request):

    liuyan = request.GET.get('liuyan',None)

    if liuyan:

        liuyanbans = Liuyanban()

        liuyanbans.lyb_context = liuyan
        liuyanbans.save()
        return redirect('jade:liuyanban')

    return redirect('jade:liuyanban')




def del_liuyanban(request):
    dz_id = request.GET.get('dz_id',None)

    # print(dz_id,type(dz_id))
    if dz_id:
        # print('jinru')
        liuyanban = Liuyanban.objects.get(id=int(dz_id))
        liuyanban.delete()

        return JsonResponse({'msg':'1'})

    return JsonResponse({'msg': '0'})


def queren(request):
    passwd = request.GET.get('passwd', None)
    # print(passwd,type(passwd))
    if passwd == 'asd123456789.':
        return JsonResponse({'msg': '1'})

    return JsonResponse({'msg': '0'})



def xiagu(request):

    musics = Music.objects.filter(title__icontains="峡谷之音")
    return render(request,'xiagu.html',context={'musics':musics})

# 搜索功能
def sousuo(request):
    words = request.GET.get('words')
    # print(words)
    # print(type(words)) #str
    # 給定word1，word2初始值，防止if沒進去，後面沒定義
    # 爲什麼上面的，不用取不到就用None代替，因爲代替不了，一直都是空的字符串
    # 爲什麼下面的判斷不包含下面兩個字符串的也能搜索到，因爲是或者，它會去到後面的判斷，只要是包含空字符串的都是
    # 然而所有的都包含
    words1 = 'bxjbnxjgx3116'
    words2 = 'xnbnxnbjg7585'
    words3 = 'fnnzffjjfff88'
    if words:
        words1 = words[:4]
        words2 = words[-4:]
        # print(words1)
        # print(words2)
        # 截取中間一段
        theStart = len(words) // 3
        theEnd = (len(words) * 2) // 3
        words3 = words[theStart:theEnd]
    musics = Music.objects.filter(
                                    Q(title__icontains=words1) |
                                    Q(title__icontains=words2) |
                                    Q(title__icontains=words3) |
                                    Q(title__istartswith=words) |
                                    Q(title__icontains=words) |
                                    Q(title__in=words)
                                  )
    return render(request, 'music.html', context={'musics': musics})
