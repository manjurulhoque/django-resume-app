from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", {})


def create_resume(request):
    return render(request, "create.html", {})
