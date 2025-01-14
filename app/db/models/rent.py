from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base


class Rent(Base):
    __tablename__ = "rent"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    reader_id = Column(Integer, ForeignKey("readers.id"), nullable=False)
    rent_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)

    book = relationship("Book")
    reader = relationship("Reader", back_populates="rents")
