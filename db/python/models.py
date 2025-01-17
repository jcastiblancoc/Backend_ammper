from sqlalchemy.sql.functions import now
from connection import Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import column_property
import uuid
from sqlalchemy.dialects.postgresql import UUID

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=now())
    first_name = Column(String)
    last_name = Column(String)
    full_name = column_property(first_name + " " + last_name)
    email = Column(String)
    phone = Column(String)
    password = Column(String, nullable=False)
