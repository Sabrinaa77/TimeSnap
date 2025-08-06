from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# 個人資料
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

# 註冊
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 註冊成功後自動登入
            return redirect('profile')  # 註冊成功後導向個人頁面
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
