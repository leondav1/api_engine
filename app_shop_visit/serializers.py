from rest_framework import serializers
from .models import Store, Visit


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'title')


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('store', 'latitude', 'longtitude')
