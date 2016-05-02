#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.db import models, IntegrityError

class Delivery(models.Model):
    Delivery_ID = models.CharField(primary_key=True, max_length=8, blank=True, editable=False, null=False, verbose_name=u'Хүргэлтийн дугаар')
    Delivery_Reg_Time = models.DateTimeField(auto_now_add=True, null=False, verbose_name=u'Бүртгэгдсэн огноо')
    Delivery_Est_Date = models.DateField(null=False, verbose_name=u'Хүргэгдэх огноо')
    Delivery_Sender = models.CharField(max_length=45, null=False, verbose_name=u'Илгээгчийн нэр')
    Delivery_Sender_Phone = models.CharField(max_length=8, null=False, verbose_name=u'Илгээгчийн утасны дугаар')
    Delivery_From_Address = models.CharField(max_length=255, null=False, verbose_name=u'Илгээгчийн хаяг')
    Delivery_Recipient = models.CharField(max_length=45, null=False, verbose_name=u'Хүлээн авагчийн нэр')
    Delivery_Recipient_Phone = models.CharField(max_length=8, null=False, verbose_name=u'Хүлээн авагчийн утасны дугаар')
    Delivery_To_Address = models.CharField(max_length=255, null=False, verbose_name=u'Хүлээн авагчийн хаяг')
    Delivery_Total = models.FloatField(null=False, verbose_name=u'Нийт төлбөр')
    Status_ID = models.ForeignKey('registration.Status', verbose_name=u'Төлөв')
    #Shipment_ID = models.ForeignKey('registration.Shipment', verbose_name=u'Ачаанууд')

    def __unicode__(self):
        return u'%s' % self.Delivery_ID

    def save(self, *args, **kwargs):
        if self.Delivery_ID:
            super(Delivery, self).save(*args, **kwargs)
            return

        unique = False
        while not unique:
            try:
                self.Delivery_ID = get_random_string(length=8)
                super(Delivery, self).save(*args, **kwargs)
            except IntegrityError:
                self.Delivery_ID = get_random_string(length=8)
            else:
                unique = True

    class Meta:
        verbose_name = u'Хүргэлт'
        verbose_name_plural = u'Хүргэлтүүд'

class Status(models.Model):
    Status_ID = models.AutoField(primary_key=True, null=False, verbose_name=u'Төлөвийн дугаар')
    Status = models.CharField(max_length=45, null=False, verbose_name=u'Төлөвийн нэр')

    def __unicode__(self):
        return u'%s' % self.Status

    class Meta:
        verbose_name = u'Төлөв'
        verbose_name_plural = u'Төлвүүд'

class Type(models.Model):
    Type_ID = models.AutoField(primary_key=True, null=False, verbose_name=u'Төрлийн дугаар')
    Type = models.CharField(max_length=45, null=False, verbose_name=u'Төрлийн нэр')

    def __unicode__(self):
        return u'%s' % self.Type

    class Meta:
        verbose_name = u'Ачааны төрөл'
        verbose_name_plural = u'Ачааны төрлүүд'

class Shipment(models.Model):
    Shipment_ID = models.AutoField(primary_key=True, null=False, verbose_name=u'Ачааны дугаар')
    Shipment_Weight = models.FloatField(null=False, verbose_name=u'Ачааны жин')
    Type_ID = models.ForeignKey(Type, verbose_name=u'Ачааны төрөл')
    Shipment_Note = models.TextField(max_length=500, blank=True, verbose_name=u'Ачааны тэмдэглэл')
    Indication_ID = models.ManyToManyField('registration.Indication', verbose_name=u'Шинж чанар')
    Delivery_ID = models.ForeignKey(Delivery, verbose_name=u'Хүргэлтийн дугаар');

    def __unicode__(self):
        return u'%s' % self.Shipment_ID

    def display_indication(self):
        return u', '.join([ Indication.Indication for Indication in self.Indication_ID.all()[:3] ])

    class Meta:
        verbose_name = u'Ачаа'
        verbose_name_plural = u'Ачаанууд'

class Indication(models.Model):
    Indication_ID = models.AutoField(primary_key=True, null=False, verbose_name=u'Шинж чанарын дугаар')
    Indication = models.CharField(max_length=45, null=False, verbose_name=u'Шинж чанарын нэр')

    def __unicode__(self):
        return u'%s' % self.Indication

    class Meta:
        verbose_name = u'Шинж чанар'
        verbose_name_plural = u'Шинж чанарууд'

class State(models.Model):
    State_ID = models.AutoField(primary_key=True, null=False, verbose_name=u'Аймаг/нийслэлийн дугаар')
    State = models.CharField(max_length=45, null=False, verbose_name=u'Аймаг/нийслэлийн нэр')

    def __unicode__(self):
        return u'%s' % self.State

    class Meta:
        verbose_name = u'Аймаг/нийслэл'

class SubState(object):
    SubState_ID = models.AutoField(primary_key=True, null=False, verbose_name=u'Сум/дүүргийн дугаар')
    SubState = models.CharField(max_length=45, null=False, verbose_name=u'Сум/дүүргийн нэр')

    def __unicode__(self):
        return u'%s' % self.SubState

    class Meta:
        verbose_name = u'Сум/дүүрэг'
            
        