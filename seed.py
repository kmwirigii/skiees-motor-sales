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
