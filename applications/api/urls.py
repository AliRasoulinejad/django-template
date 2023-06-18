from django.urls import path, include


urlpatterns = [
    path("users/", include(("applications.user.urls", "user"))),
]
