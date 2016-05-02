from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Delivery, Status, Shipment, Indication

def index(request):
	return render(request, 'registration/index.html')

def about(request):
	return render(request, 'registration/about-us.html')

def services(request):
	return render(request, 'registration/services.html')

def contact(request):
	return render(request, 'registration/contact-us.html')

def delivery_detail(request):
    if 'id' in request.GET:
        identify = request.GET['id']
    	delivery = get_object_or_404(Delivery, pk=identify)
        return render(request, 'registration/view_delivery.html', {'delivery': delivery})

def report(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response