# backend/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Information(Base):
    __tablename__ = "information"

    id = Column(Integer, primary_key=True, index=True)
    lead_dbp = Column(String, index=True)
    study = Column(String, index=True)
    email = Column(String, index=True)
    study_status = Column(String, index=True)
