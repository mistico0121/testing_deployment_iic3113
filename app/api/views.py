from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from devices.models import Device
from point_of_sales.models import PointOfSale
from stores.models import Store

from .serializers import DeviceSerializer, PointOfSaleSerializer,  StoreSerializer

class DeviceListApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the Device items for given requested user
        '''
        devices = Device.objects.all().order_by('name')
        serializer = DeviceSerializer(devices, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeviceShowApiView(APIView):
    def get(self, request, point_id):
        '''
        Show all Devices from one point of sale items for given requested user
        '''
        devices = Device.objects.filter(point_of_sale=point_id)
        serializer = DeviceSerializer(devices, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class PointOfSaleListApiView(APIView):
    def get(self, request, store_id):
        '''
        List all the Points Of Sale items for given requested user
        '''
        points_of_sale = PointOfSale.objects.filter(store=store_id)
        serializer = PointOfSaleSerializer(points_of_sale, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class StoreListApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the Stores items for given requested user
        '''
        stores = Store.objects.all().order_by('name')
        serializer = StoreSerializer(stores, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)