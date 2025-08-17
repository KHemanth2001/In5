from fastapi import APIRouter, Depends
from services.content_generator import generate_short_insight, generate_long_insight
from schemas.content import KnowledgeContentResponse
from sqlalchemy.orm import Session
from db.db_connection import get_db
from fastapi import Depends
from typing import Annotated
from schemas.show_user import UserData
from services.jwt_token_generator import get_current_active_user, oauth2_scheme

router=APIRouter(
    prefix ='/generate',
    tags=['generate_content']
)

@router.get('/short_insights')
def get_short_insight(current_user: Annotated[UserData, Depends(get_current_active_user)], topic: str, db: Session = Depends(get_db)) -> KnowledgeContentResponse:
    return generate_short_insight(topic,db)

@router.get('/long_insights')
def get_long_insight(current_user: Annotated[UserData, Depends(get_current_active_user)], topic: str) -> KnowledgeContentResponse:
    return generate_long_insight(topic)

@router.get('/user')
def user(
    current_user: Annotated[UserData, Depends(get_current_active_user)],
    token: Annotated[str, Depends(oauth2_scheme)]
):
    return current_user
