from fastapi import Depends

from .services.auth import oauth2_scheme, AuthService
from .tables import User


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    return AuthService.validate_token(token)
