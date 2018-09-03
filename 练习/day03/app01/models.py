from django.db import models

# Create your models here.


class UserInfo(models.Model):#创建了一张以UserInfo为表名的表;属性对应字段，数据对应Python中的对象
    nid=models.AutoField(primary_key=True)  #AutoField对应自增长的int类型
    name=models.CharField(max_length=32)    #charfield对应varchar类型
    password=models.CharField(max_length=32,default='')
    # default='' 默认值
    # null=True 字段可以为空
    #以上两种方式选其一
    gender=models.IntegerField()  #IntegerField对应普通int整数类型
    birthday=models.DateField() #DateField对应日期类型



