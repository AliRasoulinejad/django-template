use_simple_user_app = "{{cookiecutter.use_simple_user_app}}"
use_jwt_authentication = "{{cookiecutter.use_jwt_authentication}}"

if use_simple_user_app.lower() == "n" and use_jwt_authentication.upper() == "y":
    raise "You can't set jwt without user app"
