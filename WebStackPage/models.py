# coding=utf-8


from django.db import models
from django.utils import timezone
# Create your models here.
#
class content(models.Model):
    """
    Content 链接选项
    """
    url=models.URLField()
    title=models.CharField(max_length=200,null=True,blank=True)
    desc=models.TextField(null=True,blank=True)
    create_time=models.DateTimeField(auto_now=False,default=timezone.now)
    icon_img=models.TextField("icon")
    type=models.ForeignKey("menu",on_delete=models.CASCADE,related_name="content")
    def __unicode__(self):
        return self.title
    class Meta:
        db_table="map_content"


class menu(models.Model):
    """
    Menu 侧边菜单
    """
    title=models.CharField(max_length=200)
    # href_id=models.CharField(max_length=150)
    icon_style=models.CharField(max_length=100)
    create_time=models.DateTimeField(auto_now=False,default=timezone.now)

    def __unicode__(self):
        return self.url
    class Meta:
        db_table="map_menu"