#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

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
    email = Column(String)
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

    def __repr__(self):
        return f'<Car {self.year} {self.make} {self.model}>'

# Database setup
engine = create_engine('sqlite:///skiees_motors.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def seed_database():
    try:
        session.query(Car).delete()
        session.query(Customer).delete()
        session.query(Company).delete()
        session.commit()

        skiees = Company(name="Skiees Motors", founding_year=2010)
        session.add(skiees)
        session.commit()  

        
        customers = [
            Customer(name="John Kamau", phone="254712345678", email="john@example.com", company_id=skiees.id),
            Customer(name="Mary Wanjiku", phone="254723456789", email="mary@example.com", company_id=skiees.id),
            Customer(name="James Mwangi", phone="254734567890", email="james@example.com", company_id=skiees.id)
        ]
        session.add_all(customers)
        session.commit()  

        cars = [
            Car(make="Toyota", model="Corolla", year=2020, price=2500000, company_id=skiees.id),
            Car(make="Subaru", model="Forester", year=2019, price=3200000, company_id=skiees.id),
            Car(make="Nissan", model="X-Trail", year=2021, price=2800000, company_id=skiees.id),
            Car(make="Mitsubishi", model="Pajero", year=2018, price=3500000, company_id=skiees.id)
        ]
        session.add_all(cars)
        session.commit()

        print("Database seeded successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error seeding database: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    seed_database()