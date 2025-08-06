from django.contrib import admin

# Register your models here.
from .models import AvailableSlot, Reserve

admin.site.register(AvailableSlot)
admin.site.register(Reserve)
