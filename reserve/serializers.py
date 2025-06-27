from rest_framework import serializers
from .models import Reserve

class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = ['id', 'name', 'telephone', 'reserve_date', 'reserve_time']
