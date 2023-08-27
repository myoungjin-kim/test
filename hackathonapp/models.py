

# Create your models here.
from django.db import models

class GC(models.Model):
    no = models.AutoField(db_column='no', primary_key=True)
    date = models.CharField(db_column='date', max_length=255)
    top = models.CharField(db_column='top', max_length=255)
    bottom = models.CharField(db_column='bottom', max_length=255)
    vehicle = models.IntegerField(db_column='vehicle')
    inout = models.IntegerField(db_column='inout')
    high = models.FloatField(db_column='high',null=True, blank=True) # null blank 필수
    low = models.FloatField(db_column='low',null=True, blank=True)
    now = models.FloatField(db_column='now',null=True, blank=True)
    hum = models.FloatField(db_column='hum',null=True, blank=True)
    rain = models.FloatField(db_column='rain',null=True, blank=True)
    prob = models.FloatField(db_column='prob',null=True, blank=True)
    @classmethod
    def get_row_count(cls):
        return cls.objects.count()


    class Meta:
            db_table = 'get'#테이블 이름 get으로 설정해서 만들어줌