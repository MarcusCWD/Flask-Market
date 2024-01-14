from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Replace the connection parameters with your MariaDB credentials and database name
DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)  # Specify a length, for example, 50 characters
    email = Column(String(100), unique=True, index=True)    # Adjust the length as needed
    password = Column(String(255))  # Specify a length, for example, 255 characters

    posts = relationship('Post', back_populates='author')

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)  # Adjust the length as needed
    body = Column(String(1000))  # Specify a length, for example, 1000 characters
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship('User', back_populates='posts')

Base.metadata.create_all(bind=engine)
