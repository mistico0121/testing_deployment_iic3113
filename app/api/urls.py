from django.conf.urls import url
from django.urls import re_path, path, include
from .views import DeviceListApiView, PointOfSaleListApiView, StoreListApiView, DeviceShowApiView


urlpatterns = [
    path('devices/', DeviceListApiView.as_view()),
    path('devices/<int:point_id>/', DeviceShowApiView.as_view()),
    path('points_of_sale/<int:store_id>/', PointOfSaleListApiView.as_view()),
    path('stores', StoreListApiView.as_view()),
]