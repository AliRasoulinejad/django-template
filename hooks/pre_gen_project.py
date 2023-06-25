use_simple_user_app = "{{cookiecutter.use_simple_user_app}}"
use_jwt = "{{cookiecutter.use_jwt}}"

if use_simple_user_app.lower() == "n" and use_jwt.upper() == "y":
    raise "You can't set jwt without user app"
