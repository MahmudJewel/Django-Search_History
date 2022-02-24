from django.urls import path, include
from .views import history_view

urlpatterns = [
    path('', history_view.as_view()),
]
