from . import views
from django.urls import path

app_name = 'reserve'

urlpatterns = [
    path('', views.home, name='home'),
]

