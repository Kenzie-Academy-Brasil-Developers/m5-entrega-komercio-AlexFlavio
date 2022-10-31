from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path("accounts/", views.AccountView.as_view()),
    path("accounts/newest/<int:num>/", views.AccountListView.as_view()),
    path("accounts/<pk>/", views.AccountUpdateView.as_view()),
    path("accounts/<pk>/management/", views.AccountDeleteView.as_view()),
    path("login/", views.LoginView.as_view()),
]
