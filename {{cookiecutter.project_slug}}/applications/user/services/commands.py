from applications.user.models import User
from result import Result


def user_register(*, username: str, password: str, **extra_fields) -> Result[User, str]:
    return User.objects.create_user(username=username, password=password, **extra_fields)
