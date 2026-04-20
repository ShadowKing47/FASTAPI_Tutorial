# Database engine, session factory, and declarative Base shared across all ORM models.
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

engine = create_engine(
    DATABASE_URL,
    # SQLite requires this flag when used with FastAPI's threaded request handling
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    # FastAPI dependency: yields a session and closes it when the request finishes
    with SessionLocal() as db:
        yield db
