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

    def __init__(self, id, nums, numsp, date, time):
        id.self = id
        nums.self = nums
        numsp.self = numsp
        date.self = date
        time.self = time