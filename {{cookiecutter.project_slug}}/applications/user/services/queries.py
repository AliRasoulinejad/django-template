from applications.user.models import User
from result import Result, Ok, Err


def user_retrieve(*, username: str) -> Result[User, str]:
    try:
        user = User.objects.get(username=username)

        return Ok(user)
    except Exception:
        return Err("user with this username not found")
