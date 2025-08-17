from db.db_connection import Base
from sqlalchemy import Column, String, Integer, DateTime, func, Nullable


class User(Base):
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    password = Column(String)
    created_at = Column(DateTime, default=func.now())
    last_login = Column(DateTime, nullable =True)


