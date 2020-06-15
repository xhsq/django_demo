from django.urls.conf import re_path
from . import views

urlpatterns = [
    re_path('', views.setcook),
    re_path('', views.getcook),
]