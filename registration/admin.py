#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Delivery, Status, Shipment, Indication, Type

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('Delivery_ID', 'Delivery_Reg_Time', 'Delivery_Est_Date', 'Delivery_Sender', 'Delivery_Recipient', 'Delivery_Total')

class StatusAdmin(admin.ModelAdmin):
	list_display = ('Status_ID', 'Status')

class ShipmentAdmin(admin.ModelAdmin):
	list_display = ('Shipment_ID', 'Shipment_Weight', 'Shipment_Note', 'display_indication')

class IndicationAdmin(admin.ModelAdmin):
	list_display = ('Indication_ID', 'Indication')

class TypeAdmin(admin.ModelAdmin):
	list_display = ('Type_ID', 'Type')

admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(Indication, IndicationAdmin)
admin.site.register(Type, TypeAdmin)