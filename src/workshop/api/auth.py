from fastapi import APIRouter, Depends, Body
from fastapi.security import OAuth2PasswordRequestForm

from ..dependencies import get_current_user
from ..models.auth import Token, UserCreate, User
from ..services.auth import AuthService

router = APIRouter(prefix='/auth', tags=["Auth", ])


@router.post('/sign_up', summary='Registration', response_model=Token)
def sign_up(
        user_data: UserCreate = Body(),
        service: AuthService = Depends()
):
    return service.register_new_user(user_data)


@router.post('/sign_in', summary='Authorization', response_model=Token)
def sign_in(
        form_data: OAuth2PasswordRequestForm = Depends(),
        service: AuthService = Depends()
):
    return service.authenticate_user(form_data.username, form_data.password)


@router.get('/me', response_model=User)
def get_user(user: User = Depends(get_current_user)):
    return user
