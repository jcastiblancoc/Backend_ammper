import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DB_ADDRESS


engine = create_engine(DB_ADDRESS)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
