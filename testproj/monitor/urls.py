from django.urls import path ,re_path
from .views import upload_from_json
"""Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
urlpatterns = [
    re_path(r'^upload_json/', upload_from_json, name='upload_from_json'),
]