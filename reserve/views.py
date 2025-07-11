from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReserveForm
from .models import Reserve
from .serializers import ReserveSerializer
from rest_framework import generics
import datetime
from rest_framework import serializers
from .models import Reserve
from django.http import JsonResponse

# 首頁（可顯示所有預約）
def home(request):
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            reserve = form.save()
            return redirect('reserve:show', id=reserve.id)  # ✅ 加上 id
    else:
        reserve = Reserve.objects.all()
    return render(request, 'reserve/home.html', {'reserve': reserve})

# 查看單筆預約
def show(request, id):
    reserve = get_object_or_404(Reserve, id=id)
    if request.method == 'POST':
        form = ReserveForm(request.POST, instance=reserve)
        if form.is_valid():
            form.save()
            return redirect('reserve:show', id=reserve.id)  # ✅
    else:
        form = ReserveForm(instance=reserve)
    return render(request, 'reserve/show.html', {'form': form, 'reserve': reserve})

# 新增預約
print("✅ 收到 POST 請求：建立預約")
def new(request):
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            reserve = form.save()
            return redirect('reserve:show', id=reserve.id)  # ✅
    else:
        form = ReserveForm()
    return render(request, 'reserve/new.html', {'form': form})

# 編輯預約
def edit(request, id):
    reserve = get_object_or_404(Reserve, id=id)
    if request.method == 'POST':
        form = ReserveForm(request.POST, instance=reserve)
        if form.is_valid():
            form.save()
            return redirect('reserve:show', id=reserve.id)  # ✅
    else:
        form = ReserveForm(instance=reserve)
    return render(request, 'reserve/edit.html', {'form': form, 'reserve': reserve})

# 刪除預約
def delete(request, id):
    reserve = get_object_or_404(Reserve, id=id)
    if request.method == 'POST':
        reserve.delete()
        return redirect('reserve:home')
    return render(request, 'reserve/delete.html', {'reserve': reserve})

# 顯示日曆
def calendar_page(request):
    return render(request, 'reserve/calendar.html')

# 提供 API 資料（List）class ReserveSerializer(serializers.ModelSerializer):
class ReserveListAPIView(generics.ListAPIView):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer


class ReserveSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    start = serializers.SerializerMethodField()

    class Meta:
        model = Reserve
        fields = ['id', 'title', 'start']

    def get_title(self, obj):
        return f"{obj.name} 預約"

    def get_start(self, obj):
        dt = datetime.datetime.combine(obj.reserve_date, obj.reserve_time)
        return dt.isoformat()

# 建立預約（獨立頁面）
def create_reservation(request):
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            reserve = form.save()
            return redirect('reserve:show', id=reserve.id)
    else:
        form = ReserveForm()
    return render(request, 'reserve/form.html', {'form': form})




def reserve_events(request):
    data = [
        {
            "title": f"{r.name} 預約",
            "start": f"{r.reserve_date}T{r.reserve_time}",
        }
        for r in Reserve.objects.all()
    ]
    return JsonResponse(data, safe=False)
