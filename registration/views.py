from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.utils import timezone
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Delivery, Status, Shipment, Indication
from .forms import ContactForm
from news.models import Post
from rest_framework import viewsets
from .serializers import DeliverySerializer

def index(request):
    posts = Post.objects.order_by('-Published_Date')[0:3]
    return render(request, 'registration/index.html', {'posts': posts})

def about(request):
    posts = Post.objects.order_by('-Published_Date')[0:3]
    return render(request, 'registration/about-us.html', {'posts': posts})

def services(request):
    posts = Post.objects.order_by('-Published_Date')[0:3]
    return render(request, 'registration/services.html', {'posts': posts})

def contact_us(request):
    posts = Post.objects.order_by('-Published_Date')[0:3]
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['the.ganzorig25@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "contact_form/contact_form.html", {'posts': posts, 'form': form})

def thanks(request):
    posts = Post.objects.order_by('-Published_Date')[0:3]
    return render(request, 'contact_form/contact_form_sent.html', {'posts': posts})

def delivery_detail(request):
    posts = Post.objects.order_by('-Published_Date')[0:3]
    if 'id' in request.GET:
        identify = request.GET['id']
    	delivery = get_object_or_404(Delivery, pk=identify)
        return render(request, 'registration/view_delivery.html', {'delivery': delivery, 'posts': posts})

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

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all().order_by('-Delivery_Reg_Time')
    serializer_class = DeliverySerializer