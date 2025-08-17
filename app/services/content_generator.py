# schemas/content.py
from prompts import templates
from utils.gemini import call_gemini
from schemas.content import KnowledgeContentResponse
from crud.db_interactions import save_knowledge
from fastapi import Depends
from sqlalchemy.orm import Session
from db.db_connection import get_db

def generate_short_insight(topic: str, db: Session) -> KnowledgeContentResponse:
    prompt=templates.SHORT_PROMPT_TEMPLATE.format(topic=topic)
    result=call_gemini(prompt)
    save_knowledge(result, db)
    return KnowledgeContentResponse(
            title= result['title'],
            content=result['content'],
            topics=result['topics']
        )

def generate_long_insight(topic: str, db: Session) -> KnowledgeContentResponse:
    prompt=templates.DEEP_DIVE_PROMPT_TEMPLATE.format(topic=topic)
    result = call_gemini(prompt)
    save_knowledge(result, db)
    return KnowledgeContentResponse(
        title=result['title'],
        content=result['content'],
        topics=result['topics']
    )