from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    cars = relationship('Car', backref='company')
    customers = relationship('Customer', backref='company')

    def __repr__(self):
        return f'<Company {self.name}>'

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    phone = Column(String())
    email = Column(String())
    company_id = Column(Integer(), ForeignKey('companies.id'))

    cars = relationship('Car', backref='customer')

    def __repr__(self):
        return f'<Customer {self.name}>'

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer(), primary_key=True)
    make = Column(String())
    model = Column(String())
    year = Column(Integer())
    price = Column(Integer())  # in KSH
    company_id = Column(Integer(), ForeignKey('companies.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))

    def __repr__(self):
        return f'<Car {self.year} {self.make} {self.model}>'