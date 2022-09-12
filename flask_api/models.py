from types import NoneType
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
    
    def obj_to_dict(self):
        if isinstance(self.nums, str):
            self.nums = [int(x) for x in self.nums.split(",")]
        if isinstance(self.numsp, str):
            self.numsp = [int(x) for x in self.numsp.split(",")]
        return {
            "lottery": self.__tablename__,
            "id": self.id,
            "lotto": self.nums,
            "lotto_plus": self.numsp,
            "date": self.date,
            "time": self.time
            }