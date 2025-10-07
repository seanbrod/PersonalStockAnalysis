#Sean Broderick
from connection import engine, Base
from db_model import *


#create all tables for db
Base.metadata.create_all(bind=engine)

