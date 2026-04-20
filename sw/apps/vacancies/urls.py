from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:vacancy_id>/', views.CreateApplyView.as_view(), name='apply'),
    path('status/<int:apply_id>/', views.ChangeStatusView.as_view(), name='change_status'),
]