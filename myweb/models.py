from django.db import models

# Create your models here.
class Music(models.Model):

    title = models.CharField(max_length=100)
    thesrc = models.CharField(max_length=100)
    file_size = models.CharField(max_length=30,default='0M')


class Duanzi(models.Model):

    duanzi_context = models.TextField()



class Tupian(models.Model):

    title = models.CharField(max_length=100,default='斗图')
    imgsrc = models.CharField(max_length=255)



class Liuyanban(models.Model):

    lyTime = models.DateTimeField(auto_now_add=True)
    lyb_context = models.TextField()



