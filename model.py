from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Connection to Database i.e 'mysql+mysqlconnector://root@localhost:3307/market.db'
database_connector = 'mysql+mysqlconnector'
DATABASE_URL = (database_connector + '://'
                + os.environ.get('DATABASE_USER')
                + '@'
                + os.environ.get('DATABASE_ADDRESS')
                + ':'
                + os.environ.get('DATABASE_PORT')
                + '/'
                + os.environ.get('DATABASE_NAME'))

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()


### Declare all tables and relationships here below ###
class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer(), primary_key=True)
    name = Column(String(length=30), nullable=False, unique=True)
    price = Column(Integer(), nullable=False)
    barcode = Column(String(length=12), nullable=False, unique=True)
    description = Column(String(length=1024), nullable=False, unique=True)
