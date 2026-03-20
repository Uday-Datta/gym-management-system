from django.urls import path
from .views import dashboard_view
from .views import members_list

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('members/', members_list, name='members_list'),

]