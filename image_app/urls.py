from django.urls import path
from .views import RandomImageView
from .views import save_annotation

urlpatterns = [
    path('random-image/', RandomImageView.as_view(), name='random-image'),
    path('submit-polygons/', save_annotation),
]
