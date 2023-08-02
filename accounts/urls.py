from django.urls import path

from accounts.views import LogoutUser, RegisterView , LoginView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutUser.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]