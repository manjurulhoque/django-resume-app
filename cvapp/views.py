from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.http import HttpResponse

from .utils import render_to_pdf

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def create_resume(request):
    if request.method == "POST":
        context = {
            "context" : request.POST
        }
        pdf = render_to_pdf('pdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')
    return render(request, "create.html", {})

def pdf_view(request):

    pdf = render_to_pdf('pdf.html', {})
    return HttpResponse(pdf, content_type='application/pdf')
