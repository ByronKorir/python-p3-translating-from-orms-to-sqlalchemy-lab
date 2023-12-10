from models import Dog
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory')

def create_table(base,engine):
    base.metadata.create_all(engine)
    return engine
def save(session, dog):
    session.add(dog)
    session.commit()
    return session

def get_all(session):
    
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()
    
def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name and Dog.breed == breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.add(dog)
    session.commit()
    return session