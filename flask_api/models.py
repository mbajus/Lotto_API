from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)

class Lotto(Base):
    __tablename__ = 'lotto'

    id = Column(Integer, primary_key=True)
    nums = Column(String)
    numsp = Column(String)
    date = Column(Integer)
    time = Column(Integer)
    # ssid = Column(Integer) # SuperSzansa id, for future assignment