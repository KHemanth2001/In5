# routes/knowledge.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db_connection import get_db
from crud.db_interactions import get_knowledge_by_topic
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from typing import Annotated

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

@router.get("/knowledge/{topic}")
def read_knowledge(token: Annotated[str, Depends(oauth2_scheme)] ,topic: str, db: Session = Depends(get_db)):
    return get_knowledge_by_topic(topic, db)
