from werkzeug.security import safe_str_cmp
from resources.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):  # safe_str_cmp() helps in comparing string safely
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
