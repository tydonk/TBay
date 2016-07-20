from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    item = relationship("Item", backref="owner")
    bid = relationship("Bid", backref="bidder")
    
class Item(Base):
    __tablename__ = "item"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
    bids = relationship("Bid", backref="bid")
    
    owner_id = Column(Integer, ForeignKey('owner.id'), nullable=False)
    
class Bid(Base):
    __tablename__ = "bid"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    
    bidder_id = Column(Integer, ForeignKey('bidder.id'), nullable=False)
    bid_id = Column(Integer, ForeignKey('bid.id'), nullable=False)
    
Base.metadata.create_all(engine)

# Users should be able to auction multiple items.
# Users should be able to bid on multiple items.
# Multiple users should be able to place a bid on an item.

#RELATIONSHIPS:
    # User -> Item = ONE to MANY
    # User -> Bid = ONE to MANY
    # Item -> Bid = ONE to MANY
    
# Add three users to the database:
edward_nigma = User(username="Riddler", password="riddle_me_this")
victor_fries = User(username="MrFreeze", password="everybody_chill")
pamela_isley = User(username="PoisonIvy", password="so_little_time")

# Make one user auction a baseball:
    # 
baseball = Item(name="baseball", description="A real baseball", owner=victor_fries)

# Have each other user place two bids on the baseball:


# Perform a query to find out which user placed the highest bid:


    