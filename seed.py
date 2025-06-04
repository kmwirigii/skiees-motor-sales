#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    founding_year = Column(Integer)

    def __repr__(self):
        return f'<Company {self.name}>'

    class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)


mail = Column(String)
    company_id = Column(Integer, ForeignKey('companies.id'))

    def __repr__(self):
        return f'<Customer {self.name}>'

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)

    year = Column(Integer)
    price = Column(Integer)  # in KSH
    company_id = Column(Integer, ForeignKey('companies.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=True)
    engine = create_engine('sqlite:///skiees_motors.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def seed_database():
    try:
        pass
    finally:
        session.close()