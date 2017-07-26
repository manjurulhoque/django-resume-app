from django.conf.urls import url
from django.contrib import admin

from cvapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^create$', views.create_resume, name="create_resume"),
    url(r'^pdf$', views.some_view),
]
