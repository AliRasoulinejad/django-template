from django.urls import path

from .apis import UserRegisterApi, UserSelfApi

urlpatterns = [
    path("self", UserSelfApi.as_view(), name="self"),
    path("register", UserRegisterApi.as_view(), name="register"),
]
