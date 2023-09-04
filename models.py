from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import ipdb

Base = declarative_base()
create_engine = create_engine ("sqlite:///Restaurant.db")
session = sessionmaker(bind=create_engine)
session = session()

Restaurant_Customer = Table('restaurant_customer', Base.metadata, Column('customer_id', ForeignKey('customer.id'), primary_key = True), Column('restaurant_id', ForeignKey('restaurant.id'), primary_key = True))

class Customer(Base):

    __tablename__ ='customer'
    id = Column(Integer(),primary_key = True)
    first_name = Column(String())
    last_name = Column(String())
    reviews= relationship('Reviews',backref=backref('customers'))
    restaurant= relationship('Restaurant', secondary=Restaurant_Customer, back_populates='customer')

class Restaurant(Base):
    __tablename__ = 'restaurants'  # Table name

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship('Reviews', backref= backref('restaurant'))
    customers= relationship('Customer',secondary=Restaurant_Customer, back_populates='restaurant')

class Reviews(Base) :
        
    __tablename__ = 'reviews'
    id = Column(Integer(), primary_key = True)
    star_rating = Column(Integer())  
    Customer_id = Column(Integer(), ForeignKey('customer.id'))
    Resturant_id= Column(Integer(), ForeignKey('restaurant.id'))


Resturant1=session.query(Restaurant).first()
Customer1=session.query(Customer).first()
Review1=session.query(Reviews).first()
ipdb.set_trace()

