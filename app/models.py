from sqlalchemy import Column, Integer, String, Boolean

from database import Base

class MasterData(Base):
   __tablename__ = 'AlembicTest'
   Id = Column(Integer, primary_key=True, index=True)
   Name = Column(String)