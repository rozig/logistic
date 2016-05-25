from rest_framework import serializers
from .models import Delivery

class DeliverySerializer(serializers.ModelSerializer):
	class Meta:
		model = Delivery
		fields = ('Delivery_ID', 'Delivery_Reg_Time', 'Delivery_Est_Date', 'Delivery_Sender', 'Delivery_Sender_Phone', 'State_ID', 'SubState_ID', 'From_Address', 'Delivery_Recipient', 'Delivery_Recipient_Phone', 'To_State_ID', 'To_SubState_ID', 'To_Address', 'Delivery_Total', 'Status_ID', 'Status_Reason', 'Recipient_Signature', 'User')