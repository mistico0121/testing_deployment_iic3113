from rest_framework import serializers

from devices.models import Device
from point_of_sales.models import PointOfSale
from stores.models import Store

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id',
                'name',
                'model_number',
                'brand',
                'os',
                'color',
                'memory',
                'internal_memory',
                'price',
                'sale',
                'point_of_sale')

class PointOfSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointOfSale
        fields = ('id',
                'name',
                'description',
                'store')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id',
                'name',
                'description')