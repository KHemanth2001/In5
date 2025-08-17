# crud/db_interactions
from typing import Optional

from click import password_option
from sqlalchemy.orm import Session
from schemas.content import KnowledgeContentResponse
import json
from models.knowledge import Knowledge
from schemas.show_user import UserData, ShowUser
from models.users import User
from utils.hashing import Hash


def save_knowledge(request: dict, db: Session) -> KnowledgeContentResponse:
    new_record = Knowledge(title=request['title'], content=request['content'], topics=request['topics'])
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record


def get_knowledge_by_topic(topic: str, db: Session):
    data = db.query(Knowledge).filter(Knowledge.title == topic).all()
    return [
        {
            "title": k.title,
            "content": k.content,
            "topics": json.loads(k.topics)
        }
        for k in data
    ]

def add_user(request: UserData, db: Session):
    hashed_pwd=Hash.bcrypt(request.password)
    new_user = User(user_name = request.user_name, password = hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(db: Session, username: str, password) -> Optional[User]:
    user = db.query(User).filter(User.user_name == username).first()
    if not user:
        return None
    if not Hash.verify(password, user.password):
        return None
    return user

def get_user(db: Session, username: str):
    user=db.query(User).filter(User.user_name == username).first()
    if not user:
        return None
    return user




