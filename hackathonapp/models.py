from django.db import models

# Create your models here.
from django.db import models

class GC(models.Model):
    no = models.AutoField(db_column='no', primary_key=True)
    date = models.CharField(db_column='date', max_length=255)
    top = models.CharField(db_column='top', max_length=255)
    bottom = models.CharField(db_column='bottom', max_length=255)
    vehicle = models.IntegerField(db_column='vehicle')
    inout = models.IntegerField(db_column='inout')

    class Meta:
        db_table = 'get'#테이블 이름 get으로 설정해서 만들어줌