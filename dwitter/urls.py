from django.urls import path
from .views import dashboard, profile_list, profile, login, register


app_name = "dwitter"


urlpatterns = [
    path("", login, name="login"),
    path("register/", register, name="register"),
    path("dashboard/", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
]
