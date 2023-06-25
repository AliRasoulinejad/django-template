from result import Result

from applications.user.models import User


def user_register(*, username: str, password: str, **extra_fields) -> Result[User, str]:
    return User.objects.create_user(username=username, password=password, **extra_fields)
