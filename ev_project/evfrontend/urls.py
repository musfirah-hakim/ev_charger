from django.urls import path
from . import views

urlpatterns = [
    path('', views.charger_control, name='charger_control'),
    path('api/status/', views.charger_status, name='charger_status'),  # API for charger status
    path('api/update_status/', views.update_status, name='update_status'),
]
