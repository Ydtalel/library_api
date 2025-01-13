from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL)
SessionLOcal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()