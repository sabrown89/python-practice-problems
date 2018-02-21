from django.conf.urls import url
from . import views

app_name = 'appointment'
urlpatterns = [
    url(r'^search/$', views.search_appointments, name='search'),
    url(r'^create_form/$', views.create_form, name='create_form'),
    url(r'^$', views.index, name='index'),
]
