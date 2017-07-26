from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.http import HttpResponse

from .utils import render_to_pdf

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def create_resume(request):
    return render(request, "create.html", {})

def some_view(request):
    pdf = render_to_pdf('pdf.html', {})
    return HttpResponse(pdf, content_type='application/pdf')
