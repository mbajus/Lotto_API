from sqlalchemy import MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData() 
Base = declarative_base(metadata=metadata)

class Lotto(Base):
    __tablename__ = 'lotto'

    id = Column(Integer, nullable=False, primary_key=True)
    nums1 = Column(String(17), nullable=False)
    nums2 = Column(String(17))
    date = Column(Integer, nullable=False)
    time = Column(Integer)
    ss_id = Column(Integer, ForeignKey('superszansa.id'))
    superszansa = relationship("Superszansa")
    
    def obj_to_dict(self):
        if isinstance(self.nums1, str):
            self.nums1 = [int(x) for x in self.nums1.split(",")]
        if isinstance(self.nums2, str):
            self.nums2 = [int(x) for x in self.nums2.split(",")]
        return {
            "lottery": self.__tablename__,
            "id": self.id,
            "lotto": self.nums1,
            "lotto_plus": self.nums2,
            "date": self.date,
            "time": self.time
            }

class Minilotto(Base):
    __tablename__ = 'minilotto'

    id = Column(Integer, nullable=False, primary_key=True)
    nums1 = Column(String(14), nullable=False)
    date = Column(Integer, nullable=False)
    time = Column(Integer)
    ss_id = Column(Integer, ForeignKey('superszansa.id'))
    superszansa = relationship("Superszansa")
    
    def obj_to_dict(self):
        return {
            "lottery": self.__tablename__,
            "id": self.id,
            "minilotto": self.nums1,
            "date": self.date,
            "time": self.time
            }

class Multimulti(Base):
    __tablename__ = 'multimulti'

    id = Column(Integer, primary_key=True)
    nums1 = Column(String(59))
    nums2 = Column(String(2))
    date = Column(Integer)
    time = Column(Integer)
    ss_id = Column(Integer, ForeignKey('superszansa.id'))
    superszansa = relationship("Superszansa")
    
    def obj_to_dict(self):
        return {
            "lottery": self.__tablename__,
            "id": self.id,
            "multimulti": self.nums1,
            "plus": self.nums2,
            "date": self.date,
            "time": self.time
            }

class Euro(Base):
    __tablename__ = 'euro'

    id = Column(Integer, primary_key=True)
    nums1 = Column(String(59))
    date = Column(Integer)
    time = Column(Integer)
    ss_id = Column(Integer, ForeignKey('superszansa.id'))
    superszansa = relationship("Superszansa")
    
    def obj_to_dict(self):
        return {
            "lottery": self.__tablename__,
            "id": self.id,
            "eurojackpot": self.nums1,
            "date": self.date,
            "time": self.time
            }

class Ekstrapensja(Base):
    __tablename__ = 'ekstrapensja'

    id = Column(Integer, nullable=False, primary_key=True)
    nums1 = Column(String(17), nullable=False)
    nums2 = Column(String(17))
    date = Column(Integer, nullable=False)
    time = Column(Integer)
    ss_id = Column(Integer, ForeignKey('superszansa.id'))
    superszansa = relationship("Superszansa")
    
    def obj_to_dict(self):
        return {
            "lottery": self.__tablename__,
            "id": self.id,
            "ekstra pensja": self.nums1,
            "ekstra premia": self.nums2,
            "date": self.date,
            "time": self.time
            }

class Kaskada(Base):
    __tablename__ = 'kaskada'

    id = Column(Integer, nullable=False, primary_key=True)
    nums1 = Column(String(35), nullable=False)
    date = Column(Integer, nullable=False)
    time = Column(Integer)
    ss_id = Column(Integer, ForeignKey('superszansa.id'))
    superszansa = relationship("Superszansa")
    
    def obj_to_dict(self):
        return {
            "lottery": self.__tablename__,
            "id": self.id,
            "kaskada": self.nums1,
            "date": self.date,
            "time": self.time
            }

class Superszansa(Base):
    __tablename__ = 'superszansa'

    id = Column(Integer, nullable=False, primary_key=True)
    nums1 = Column(String(13), nullable=False)
    date = Column(Integer, nullable=False)
    time = Column(Integer)
    
    def obj_to_dict(self):
        return {
            "lottery": self.__tablename__,
            "id": self.id,
            "superszansa": self.nums1,
            "date": self.date,
            "time": self.time
            }