# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Comments(models.Model):
    commentid = models.AutoField(db_column='commentID', primary_key=True)  # Field name made lowercase.
    commentdate = models.DateField(db_column='commentDate', blank=True, null=True)  # Field name made lowercase.
    commenttime = models.TimeField(db_column='commentTime', blank=True, null=True)  # Field name made lowercase.
    commenter = models.CharField(max_length=20, blank=True, null=True)
    commenterurl = models.CharField(db_column='commenterUrl', max_length=250, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(max_length=1000, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'


class Keywords(models.Model):
    keyid = models.IntegerField(db_column='keyid')
    url = models.CharField(max_length=250, blank=True, null=True)
    term = models.CharField(max_length=20)
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keywords'
        unique_together = (('keyid', 'term'),)


class Lsi(models.Model):
    lsiid = models.IntegerField(db_column='lsiid')
    url = models.CharField(max_length=250, blank=True, null=True)
    topic = models.IntegerField()
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lsi'
        unique_together = (('lsiid', 'topic'),)


class Lsistatistic(models.Model):
    class_field = models.CharField(db_column='class', max_length=10)  # Field renamed because it was a Python reserved word.
    topic = models.IntegerField()
    mean = models.FloatField(blank=True, null=True)
    std = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lsiStatistic'
        unique_together = (('class_field', 'topic'),)


class News(models.Model):
    newsid = models.AutoField(db_column='newsID', primary_key=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='class', max_length=10, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    title = models.CharField(max_length=100, blank=True, null=True)
    newsdate = models.DateField(db_column='newsDate', blank=True, null=True)  # Field name made lowercase.
    newstime = models.TimeField(db_column='newsTime', blank=True, null=True)  # Field name made lowercase.
    journalist = models.CharField(max_length=10, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    hit = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    source = models.CharField(max_length=30, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    reclass = models.CharField(max_length=10, blank=True, null=True)
    cluster = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class News2(models.Model):
    newsid = models.IntegerField(db_column='newsID', primary_key=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='class', max_length=10, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    title = models.CharField(max_length=100, blank=True, null=True)
    newsdate = models.DateField(db_column='newsDate', blank=True, null=True)  # Field name made lowercase.
    newstime = models.TimeField(db_column='newsTime', blank=True, null=True)  # Field name made lowercase.
    journalist = models.CharField(max_length=10, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    hit = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    source = models.CharField(max_length=30, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    reclass = models.CharField(max_length=10, blank=True, null=True)
    cluster = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news2'


class Newsraw(models.Model):
    newsrawid = models.AutoField(db_column='newsRawID', primary_key=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='class', max_length=10, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    url = models.CharField(max_length=250, blank=True, null=True)
    newsraw = models.TextField(db_column='newsRaw', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsRaw'
