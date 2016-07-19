from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

user_auction_items_table = Table('user_auction_items_association', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('item_id', Integer, ForeignKey('item.id'))
)
    
class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    auction_items = relationship("Item", secondary="user_auction_items_association", backref="users")

class Item(Base):
    __tablename__ = "item"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
class Bid(Base):
    __tablename__ = "bid"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    
Base.metadata.create_all(engine)

# Users should be able to auction multiple items.
# Users should be able to bid on multiple items.
# Multiple users should be able to place a bid on an item.

#RELATIONSHIPS:
    # User -> Item = MANY to ONE
    # User -> Bid = MANY to ONE
    # Item -> Bid = MANY to MANY
    
# Add three users to the database:

# Make one user auction a baseball:

# Have each other user place two bids on the baseball:

# Perform a query to find out which user placed the highest bid:
    