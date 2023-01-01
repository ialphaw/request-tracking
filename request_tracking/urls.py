from django.urls import path

from . import views


app_name = "request_tracking"

urlpatterns = [
    path("", views.Test.as_view()),
]
