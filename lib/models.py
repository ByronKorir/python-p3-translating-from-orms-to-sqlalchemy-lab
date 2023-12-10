#!/usr/bin/env python3
from sqlalchemy import create_engine, Column, Integer, String, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)

def create_table():
    engine = create_engine('sqlite:///dogs.db')  # Use your desired database URL
    Base.metadata.create_all(engine)

def get_all(Session):
    dog = Session.query(Dog).all()
    return dog

def find_by_id(session, dog_id):
    dog = session.query(Dog).filter_by(id=dog_id).first()
    return dog

if __name__ == "__main__":
    create_table()

   