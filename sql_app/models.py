from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float

from .database import Base


class ItemEntry(Base):
    __tablename__ = "item_entries"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String)
# TODO Uncomment !!!
#    date = Column(String, unique=True)
    date = Column(String)
    price = Column(Float)


# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
#     items = relationship("Item", back_populates="owner")