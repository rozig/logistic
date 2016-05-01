#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone

class Post(models.Model):
    Author = models.ForeignKey('auth.User', verbose_name=u'Нийтлэгч')
    Title = models.CharField(max_length=200, verbose_name=u'Гарчиг')
    Text = models.TextField(verbose_name=u'Бичвэр')
    Created_Date = models.DateTimeField(default=timezone.now, verbose_name=u'Үүсгэсэн огноо')
    Published_Date = models.DateTimeField(blank=True, null=True, verbose_name=u'Нийтлэсэн огноо')
    Image = models.ImageField(upload_to='news/%Y/%m/%d/', verbose_name=u'Зураг')
    def publish(self):
        self.Published_Date = timezone.now()
        self.save()

    def __str__(self):
        return self.Title

    def __unicode__(self):
        return u'%s' % self.Title

    class Meta:
        verbose_name = u'Нийтлэл'
        verbose_name_plural = u'Нийтлэлүүд'