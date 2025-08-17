# schemas/content.py
from pydantic import BaseModel
from typing import List


class KnowledgeContentResponse(BaseModel):
    title: str
    content: str
    topics: List[str]

    class Config:
        from_attributes = True