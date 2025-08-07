from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.shortcuts import render, redirect
from .forms import RegisterForm

# 個人資料
# @login_required
def profile(request):
    user = request.user  # 取得目前登入的使用者
    return render(request, 'accounts/profile.html', {'user': user})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # 儲存使用者到資料庫
            login(request,user) # 註冊成功後自動登入
            return redirect('/accounts/profile/')  # 註冊完成後導向個人頁面
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
