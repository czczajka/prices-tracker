from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

# Hack for Heroku only because name should be postresql instead of postgres
if "postgres://" in os.environ['DATABASE_URL']:
    SQLALCHEMY_DATABASE_URL = os.environ['DATABASE_URL'].replace("://", "ql://", 1)
else:
    SQLALCHEMY_DATABASE_URL = os.environ['DATABASE_URL']

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
