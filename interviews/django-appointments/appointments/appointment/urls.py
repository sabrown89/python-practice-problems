from django.conf.urls import url
from . import views

app_name = 'appointment'
urlpatterns = [
    url(r'^search/$', views.search_appointments, name='search'),
    url(r'^$', views.index, name='index'),
]
