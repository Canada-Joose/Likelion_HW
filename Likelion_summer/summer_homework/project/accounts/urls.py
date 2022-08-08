from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    # /accounts/ 인 상태인 것이지
    path('', views.home, name='home'),
]
