from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Owner(Base):
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    pets = relationship("Pet", back_populates="owner")

class Pet(Base):
    __tablename__ = 'pets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String)
    owner_id = Column(Integer, ForeignKey('owners.id'))
    owner = relationship("Owner", back_populates="pets")
    vaccinations = relationship("Vaccination", back_populates="pet")

class Vaccination(Base):
    __tablename__ = 'vaccinations'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(String)
    pet_id = Column(Integer, ForeignKey('pets.id'))
    pet = relationship("Pet", back_populates="vaccinations")
