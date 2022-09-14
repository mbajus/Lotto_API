from types import NoneType
from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


metadata = MetaData()
Base = declarative_base(metadata=metadata)

class Lotto(Base):
    __tablename__ = 'lotto'

    id = Column(Integer, primary_key=True)
    nums1 = Column(String)
    nums2 = Column(String)
    date = Column(Integer)
    time = Column(Integer)
    # ssid = Column(Integer)
    
    def obj_to_dict(self):
        if isinstance(self.nums, str):
            self.nums1 = [int(x) for x in self.nums1.split(",")]
        if isinstance(self.numsp, str):
            self.nums2 = [int(x) for x in self.nums2.split(",")]
        return {
            "lottery": self.__tablename__,
            "id": self.id,
            "lotto": self.nums1,
            "lotto_plus": self.nums2,
            "date": self.date,
            "time": self.time
            }

# class Multi(Base):
#     __tablename__ = 'multi'

#     id = Column(Integer, primary_key=True)
#     nums1 = Column(String)
#     nums2 = Column(String)
#     date = Column(Integer)
#     time = Column(Integer)
#     # ssid = Column(Integer) # SuperSzansa id, for future assignment
    
#     def obj_to_dict(self):
#         return {
#             "lottery": 'multimulti',
#             "id": self.id,
#             "multimulti": self.nums1,
#             "plus": self.nums2,
#             "date": self.date,
#             "time": self.time
#             }

# class Multi2(Base):
#     __tablename__ = 'multi2'
#     __bind_key__ = 'multi2'

#     id = Column(Integer, primary_key=True)
#     nums1 = Column(String)
#     nums2 = Column(String)
#     date = Column(Integer)
#     time = Column(Integer)
#     # ssid = Column(Integer) # SuperSzansa id, for future assignment
    
#     def obj_to_dict(self):
#         return {
#             "lottery": 'multimulti',
#             "id": self.id,
#             "multimulti": self.nums1,
#             "plus": self.nums2,
#             "date": self.date,
#             "time": self.time
#             }