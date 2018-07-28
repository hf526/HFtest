from flask import (
    request,
)

def sign_user():
    username = request.args.get("username")
    password = request.args.get("password")
    sign = dict (
        username = username,
        password = password,
    )
    return sign