from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.db.session import engine, Base

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        print("Connected to the database successfully!")
    except Exception as e:
        print("Failed to connect to the database:", e)


@app.get('/')
async def root():
    return {'message': 'Wellcome to Library API'}
