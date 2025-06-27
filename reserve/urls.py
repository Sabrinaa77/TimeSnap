from . import views
from django.urls import path
from .views import ReserveListAPIView
from reserve.views import calendar_page

app_name = 'reserve'


urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('show/<uuid:id>/', views.show, name='show'),
    path('edit/<uuid:id>/', views.edit, name='edit'),
    path('api/reserve/', ReserveListAPIView.as_view(), name='reservae-list'),
    path('calendar/', calendar_page, name='calendar-page'),
]

