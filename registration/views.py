from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Delivery, Status, Shipment, Indication

def index(request):
	return render(request, 'registration/index.html')

def delivery_detail(request):
    if 'id' in request.GET:
        identify = request.GET['id']
    	delivery = get_object_or_404(Delivery, pk=identify)
        return render(request, 'registration/view_delivery.html', {'delivery': delivery})
    