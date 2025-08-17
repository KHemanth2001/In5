from fastapi import FastAPI
from app.routes import ai, knowledge, authentication
import uvicorn
from db.db_connection import Base, engine




app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(ai.router)
app.include_router(knowledge.router)
app.include_router(authentication.router)

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=9000,reload=True)