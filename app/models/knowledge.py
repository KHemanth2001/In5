#models/knowledge.py
# import traceback
# print("\n[DEBUG] Loading knowledge.py")
# traceback.print_stack()
from sqlalchemy import Column, Integer, String, DateTime, func, JSON
from db.db_connection import Base

class Knowledge(Base):
    __tablename__ = "knowledge"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    topics = Column(JSON, index=True)
    created_at = Column(DateTime, default=func.now())