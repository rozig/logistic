#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Delivery(models.Model):
    Delivery_ID = models.IntegerField(primary_key=True, null=False, verbose_name=u'Хүргэлтийн дугаар')
    Delivery_Reg_Time = models.DateTimeField(auto_now_add=True, null=False, verbose_name=u'Бүртгэгдсэн огноо')
    Delivery_Est_Date = models.DateField(null=False, verbose_name=u'Хүргэгдэх огноо')
    Delivery_Sender = models.CharField(max_length=45, null=False, verbose_name=u'Илгээгчийн нэр')
    Delivery_Sender_Phone = models.CharField(max_length=8, null=False, verbose_name=u'Илгээгчийн утасны дугаар')
    Delivery_From_Address = models.CharField(max_length=255, null=False, verbose_name=u'Илгээгчийн хаяг')
    Delivery_Recipient = models.CharField(max_length=45, null=False, verbose_name=u'Хүлээн авагчийн нэр')
    Delivery_Recipient_Phone = models.CharField(max_length=8, null=False, verbose_name=u'Хүлээн авагчийн утасны дугаар')
    Delivery_To_Address = models.CharField(max_length=255, null=False, verbose_name=u'Хүлээн авагчийн хаяг')
    Delivery_Total = models.FloatField(null=False, verbose_name=u'Нийт төлбөр')
    Status_ID = models.ForeignKey('registration.Status')
    Shipment_ID = models.ManyToManyField('registration.Shipment')

    def __unicode__(self):
        return u'%s' % self.Delivery_ID

    class Meta:
        verbose_name = u'Хүргэлт'
        verbose_name_plural = u'Хүргэлтүүд'

class Status(models.Model):
    Status_ID = models.IntegerField(primary_key=True, null=False, verbose_name=u'Төлөвийн дугаар')
    Status = models.CharField(max_length=45, null=False, verbose_name=u'Төлөвийн нэр')

    def __unicode__(self):
        return u'%s' % self.Status

    class Meta:
        verbose_name = u'Төлөв'
        verbose_name_plural = u'Төлвүүд'

class Shipment(models.Model):
    Shipment_ID = models.IntegerField(primary_key=True, null=False, verbose_name=u'Ачааны дугаар')
    Shipment_Piece = models.IntegerField(null=False, verbose_name=u'Ачааны тоо')
    Shipment_Weight = models.FloatField(null=False, verbose_name=u'Ачааны жин')
    Shipment_Type = models.CharField(max_length=45, null=False, verbose_name=u'Ачааны төрөл')
    Shipment_Note = models.TextField(max_length=500, verbose_name=u'Ачааны тэмдэглэл')
    Indication_ID = models.ManyToManyField('registration.Indication', verbose_name=u'Шинж чанар')

    def __unicode__(self):
        return u'%s' % self.Shipment_ID

    def display_indication(self):
        return u', '.join([ Indication.Indication for Indication in self.Indication_ID.all()[:3] ])

    class Meta:
        verbose_name = u'Ачаа'
        verbose_name_plural = u'Ачаанууд'

class Indication(models.Model):
    Indication_ID = models.IntegerField(primary_key=True, null=False, verbose_name=u'Шинж чанарын дугаар')
    Indication = models.CharField(max_length=45, null=False, verbose_name=u'Шинж чанарын нэр')

    def __unicode__(self):
        return u'%s' % self.Indication

    class Meta:
        verbose_name = u'Шинж чанар'
        verbose_name_plural = u'Шинж чанарууд'