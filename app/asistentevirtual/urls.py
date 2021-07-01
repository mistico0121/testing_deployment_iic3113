"""asistentevirtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers

from pages.views import home_view
from devices.views import device_index_view, device_show_view, device_create_view, device_update_view, device_delete_view
from point_of_sales.views import point_of_sale_index_view, point_of_sale_show_view, point_of_sale_create_view, point_of_sale_update_view, point_of_sale_delete_view

from stores.views import Store_list, store_show_view, Store_create, Store_update, Store_delete
from registration.views import Salesman_list
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from attendance_tablets.views import attendance_tablet_index_view, attendance_tablet_show_view, attendance_tablet_create_view, attendance_tablet_update_view, attendance_tablet_delete_view

from videocalls.views import videocall_index_view, videocall_middleware, videocall_delete, surveys, survey_create

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('devices/', device_index_view, name='device-index'),
    path('devices/<int:id>', device_show_view, name='device-show'),
    path('devices/create', device_create_view, name='device-create'),
    path('devices/<int:id>/update/', device_update_view, name='device-update'),
    path('devices/<int:id>/delete/', device_delete_view, name='device-delete'),

    path('point_of_sales/', point_of_sale_index_view, name='point_of_sale-index'),
    path('point_of_sales/<int:id>', point_of_sale_show_view, name='point_of_sale-show'),
    path('point_of_sales/create', point_of_sale_create_view, name='point_of_sale-create'),
    path('point_of_sales/<int:id>/update/', point_of_sale_update_view, name='point_of_sale-update'),
    path('point_of_sales/<int:id>/delete/', point_of_sale_delete_view, name='point_of_sale-delete'),

    path('attendance-tablets/', attendance_tablet_index_view, name='attendance_tablet-index'),
    path('attendance-tablets/<int:id>', attendance_tablet_show_view, name='attendance_tablet-show'),
    path('attendance-tablets/create', attendance_tablet_create_view, name='attendance_tablet-create'),
    path('attendance-tablets/<int:id>/update/', attendance_tablet_update_view, name='attendance_tablet-update'),
    path('attendance-tablets/<int:id>/delete/', attendance_tablet_delete_view, name='attendance_tablet-delete'),

    path('stores/',Store_list.as_view(),name="store-index"),
    path('stores/<int:id>', store_show_view, name='store-show'),
    path('stores/create', Store_create.as_view(), name='store-create'),
    path('stores/<int:pk>/update/', Store_update.as_view(), name='store-update'),
    path('stores/<int:pk>/delete/', Store_delete.as_view(), name='store-delete'),
    
    path('videocalls/', videocall_index_view, name='videocall-index'),
    path('makevideocall/', videocall_middleware, name='videocall-middleware'),
    path('surveys/', surveys, name='surveys'),
    path('surveys/create', survey_create, name='surveys-create'),

    
    #admin views
    path('salesmans/',Salesman_list.as_view(),name="salesman-index"),
    # paths de auth
    path('accounts/password_change/',
    PasswordChangeView.as_view(success_url = reverse_lazy('home')),
    name="account_change_password"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('registration.urls')),

    


    path('<int:data>/deletevideocall/', videocall_delete, name='videocall-delete'),

]
