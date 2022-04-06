from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Table, event
from sqlalchemy.orm import relationship, backref
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)
    resMovies = relationship("Movie", backref="users", passive_deletes=True, passive_updates=True)
class Movie(Base):
    __tablename__ = "moviesCatalog"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    genre = Column(String)
    score = Column(Float)
    price = Column(Float)
    release = Column(Boolean, default=False)
    seller_uid = Column(String, ForeignKey('users.username', onupdate='CASCADE', ondelete='CASCADE'))

@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()