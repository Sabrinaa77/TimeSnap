from django.db import models
from datetime import date, time
import uuid


# Create your models here.

class AvailableSlot(models.Model):
    date = models.DateField()
    time = models.TimeField()
    is_holiday = models.BooleanField(default=False)

    class Meta:
        unique_together = ('date', 'time')  # 同一時間只能有一筆
        ordering = ['date', 'time']

    def __str__(self):
        return f"{self.date} {self.time} - {'可預約' if self.is_available else '已關閉'}"


class Reserve(models.Model):
    slot = models.ForeignKey(AvailableSlot, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True) 
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20) 
    reserve_date = models.DateField(default=date(2025, 7, 1))  # 修正這裡
    reserve_time = models.TimeField(default=time(8, 0))
    is_active = models.BooleanField(default=True)  # 控制開關

    def __str__(self):
        return f"{self.name} - {self.reserve_date} {self.reserve_time}"



