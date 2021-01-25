from django.db import models

# Create your models here.

class Msg(models.Model):
    usr_msg = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    no = models.AutoField(primary_key=True)

    class Meta:
        managed = True,
        db_table = 'msg'
