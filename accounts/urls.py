# from django.urls import path
# from . import views

# app_name = "accounts"

# urlpatterns = [
#     path('login/', views.login, name='login'),
#     path('logout/', views.logout, name='logout'),
#     path('profile/', views.profile, name='profile'),  # 登入後才能看的頁面
#     path('register/', views.register, name='register'),
# ]

from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),  # 內建登入登出
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login')
]
