from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from app.db.session import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    biography = Column(String, nullable=True)
    birth_date = Column(Date, nullable=True)

    books = relationship("Book", back_populates="authors")
