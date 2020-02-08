from django.contrib import admin
from django.urls import path, include # 추가
from rest_framework.authtoken import views

urlpatterns = [
    path('demo/', include('demo.urls')), # demo.urls : demo 폴더 밑의 urls.py
    path('admin/', admin.site.urls),
    path('auth/', views.obtain_auth_token)
]