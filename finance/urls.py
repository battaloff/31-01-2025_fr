from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_client/', views.add_client, name='add_client'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('add_income/', views.add_income, name='add_income'),
    path('detail/', views.detail_view, name='detail'),
    path('delete/<str:model_name>/<int:record_id>/', views.delete_record, name='delete_record'),
]