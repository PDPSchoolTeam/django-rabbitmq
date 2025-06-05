from django.urls import path
from app.views import feedback_form_view, success_view

urlpatterns = [
    path("", feedback_form_view, name="feedback"),
    path("success/", success_view, name="success"),
]
