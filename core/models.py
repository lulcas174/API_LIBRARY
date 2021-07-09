from django.db import models

class Lib(models.Model):
  title = models.CharField(max_length=100,null=False,blank=False)
  publisher = models.CharField(max_length=100,null=False,blank=False)
  book_cover = models.ImageField(null=True, blank=False)
  author = models.CharField(max_length=100,null=True,blank=True)