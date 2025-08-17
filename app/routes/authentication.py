from fastapi import APIRouter, Depends
from crud.db_interactions import add_user
from sqlalchemy.orm import Session
from db.db_connection import get_db
from schemas.show_user import UserData
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from schemas.access_token import Token
from services.jwt_token_generator import login_for_access_token

router=APIRouter(
    prefix ='/authenticate',
    tags=['login'])


@router.post('/register')
def create_user(request: UserData, db: Session = Depends(get_db)):
    return add_user(request, db)


@router.post("/login", response_model=Token)
def authenicate_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session  = Depends(get_db)):
    return login_for_access_token(db,form_data)

