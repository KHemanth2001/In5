from sqlalchemy import Integer, String, DateTime, func, Column, ForeignKey
from db.db_connection import Base


class User_Preference(Base):
    __tablename__ = 'user_preferences'

    pref_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"),nullable =False)
    topic_list = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())