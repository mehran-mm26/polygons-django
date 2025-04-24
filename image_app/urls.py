from django.urls import path
from .views import RandomImageView

urlpatterns = [
    path('random-image/', RandomImageView.as_view(), name='random-image')
]
