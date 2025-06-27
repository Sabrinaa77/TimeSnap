from django.forms import ModelForm
from .models import Reserve

class ReserveForm(ModelForm):
    class Meta:
        model = Reserve
        fields = [
            'name',
            'telephone',
            'reserve_date',
            'reserve_time',
            'is_active',
        ]
        labels = {
            'name': '姓名',
            'telephone': '手機號碼',
            'reserve_date': '預約日期',
            'reserve_time': '預約時間',
        }