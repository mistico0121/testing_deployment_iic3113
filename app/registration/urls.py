from django.urls import path
from .views import SalesmanUpdate, SignUpView, delete_user

urlpatterns = [
    path('signup/',SignUpView.as_view(), name="signup"),
    path('profile/', SalesmanUpdate.as_view(), name="profile"),
    path('delete/', delete_user, name='delete-user') 
]