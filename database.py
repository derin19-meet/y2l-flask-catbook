from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_cat(name):
    cat_object = Cat(name=name)
    session.add(cat_object)
    session.commit()

def get_all_cats():
    cats = session.query(Cat).all()
    return cats

def cat_id_route(id):
    cat = session.query(Cat).filter_by(id=id).first()
    return cat

# def add_new_cat(name):
#     cat_form= Cat(name=name)
#     session.add(cat_form)
#     session.commit()