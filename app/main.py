from fastapi import FastAPI
from app.db.session import engine, Base

app = FastAPI()


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    print("Db connect!")


@app.get('/')
async def root():
    return {'message': 'Wellcome to Library API'}
