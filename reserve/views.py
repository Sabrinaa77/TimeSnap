from django.shortcuts import render

from rest_framework import generics
from .models import Reserve
from .serializers import ReserveSerializer

# Create your views here.
def home(request):
  return render(request, 'reserve/home.html')

def new(request):
  return render(request, 'reserve/new.html')

def show(request, id):
  return render(request, 'reserve/show.html', {'id': id})

def edit(request, id):
  return render(request, 'reserve/edit.html', {'id': id})

def delete(request,id):
  return render(request, 'reserve/delete.html', {'id': id})

def calendar_page(request):
    return render(request, 'reserve/calendar.html')

class ReserveListAPIView(generics.ListAPIView):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer
