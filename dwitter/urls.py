from django.urls import path
from .views import dashboard, profile_list, profile, login


app_name = "dwitter"


urlpatterns = [
    path("", login, name="login"),
    path("dashboard/", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
]
