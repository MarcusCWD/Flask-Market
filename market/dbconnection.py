import os
from sqlalchemy import create_engine

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
