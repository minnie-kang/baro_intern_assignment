from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('verify/', views.TokenVerifyView.as_view(), name='verify'),
]
