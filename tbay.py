from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, Table, desc
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    item = relationship("Item", backref="owner")
    bid = relationship("Bid", backref="bidder")
    
class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
    bids = relationship("Bid", backref="bid")
    
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
class Bid(Base):
    __tablename__ = "bids"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    bidder_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    
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

session.add_all([edward_nigma, victor_fries, pamela_isley])
session.commit()

session.query(User).all()

# Make one user auction a baseball:
baseball = Item(name="baseball", description="A real baseball", owner=victor_fries)
session.add(baseball)
session.commit()
print("{} started an auction for {} at {}".format(baseball.owner.username, baseball.name, baseball.start_time))

# Have each other user place two bids on the baseball:
starting_bid = Bid(price = 50.00, item_id = baseball.id, bidder = victor_fries)
riddler_bid = Bid(price = 55.00, item_id = baseball.id, bidder = edward_nigma)
ivey_bid = Bid(price = 75.00, item_id = baseball.id, bidder = pamela_isley)

bid_list = [riddler_bid, ivey_bid]

session.add(starting_bid)
session.commit()

for bid in bid_list:
    print("{} bid on the {} for ${}".format(bid.bidder.username, baseball.name, bid.price))

# Perform a query to find out which user placed the highest bid:
highest_bid = session.query(Bid).order_by(desc(Bid.price)).first()
print("{} had the highest bid at ${}".format(highest_bid.bidder.username, highest_bid.price))
