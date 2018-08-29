from django.db import models


# Create your models here.

class UserInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    password=models.CharField(max_length=32,null=True)
    # default='' 默认值
    # null=True 字段可以为空
    gender = models.IntegerField()
    birthday = models.DateField()
    user_datil=models.OneToOneField(to='User_datil',to_field='nid')
    dd=models.ForeignKey(to='dd',to_field='nid')

    sss=models.ManyToManyField(to='author')

    def __str__(self):
        return self.name

