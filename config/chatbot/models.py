# from django.db import models
#
# # Create your models here.
#
# class Msg(models.Model):
#     usr_msg = models.CharField(max_length=50)
#     time = models.DateTimeField(auto_now_add=True)
#     no = models.AutoField(primary_key=True)
#
#     class Meta:
#         managed = True,
#         db_table = 'msg'
#
# class Qaset(models.Model):
#     cate1 = models.TextField(blank=True, null=True)
#     cate2 = models.TextField(blank=True, null=True)
#     q = models.TextField(db_column='Q', blank=True, null=True)  # Field name made lowercase.
#     a = models.TextField(db_column='A', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'qaset'
