from django.contrib import admin
from django.urls import path, include
from image_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('image_app.urls')),
    path('', index, name='index'),  # root route
]
