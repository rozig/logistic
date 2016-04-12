from django.shortcuts import render, get_object_or_404, HttpResponse
from django.utils import timezone
from .models import Delivery, Status, Shipment, Indication

def index(request):
	return render(request, 'registration/index.html', {})

def delivery_detail(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    return render(request, 'registration/view_delivery.html', {'delivery': delivery})

"""def get_queryset(request):
	query = request.GET.get('query')
	t = loader.get_template('registration/view_delivery.html')
	c = Context({'query': query})
	return HttpResponse(t.render(c))"""

def get_detail(request, pk):
	query = get_object_or_404(Delivery, pk=pk)
	if request.method == "POST":
		form = DeliveryForm(request.POST, instance=delivery)
	else:
		form = DeliveryForm(instance=delivery)
	return render(request, 'registration/view_delivery.html', {'form': form})