from django.urls import path
from .views import CreateApplicationView, UpdateStatusView

urlpatterns = [
    path("apply/<int:vacancy_id>/", CreateApplicationView.as_view()),
    path("status/<int:application_id>/", UpdateStatusView.as_view()),
]