from django.urls import path, include


urlpatterns = [
    path("auth/", include(("applications.authentication.urls", "auth"))),
    path("users/", include(("applications.user.urls", "user"))),
]
