#!/usr/bin/env python3

import sys
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(str(Path(__file__).parent.parent))

try:
    from lib.models import Company, Customer, Car, Base
except ImportError:
    print("Error: Could not import models. Make sure:")
    print("1. Your models.py is in the 'lib' directory")
    print("2. You have an __init__.py file in the 'lib' directory")
    print("3. You're running the script from the project root directory")
    sys.exit(1)

# Database setup
engine = create_engine('sqlite:///skiees_motors.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def display_menu():
    print("\nSkiees Motors Management System")
    print("1. Manage Companies")
    print("2. Manage Customers")
    print("3. Manage Cars")
    print("4. Exit")

def manage_companies():
    while True:
        print("\nCompany Management")
        print("1. Create Company")
        print("2. View All Companies")
        print("3. Find Company by Name")
        print("4. View Company Details")
        print("5. Delete Company")
        print("6. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter company name: ")
            year = input("Enter founding year: ")
            if year.isdigit():
                company = Company(name=name, founding_year=int(year))
                session.add(company)
                session.commit()
                print(f"Company {name} created successfully!")
            else:
                print("Invalid year. Please enter a number.")
                
        elif choice == "2":
            companies = session.query(Company).all()
            for company in companies:
                print(f"{company.id}: {company.name} (Founded: {company.founding_year})")
                
        elif choice == "3":
            name = input("Enter company name to search: ")
            companies = session.query(Company).filter(Company.name.ilike(f"%{name}%")).all()
            if companies:
                for company in companies:
                    print(f"{company.id}: {company.name}")
            else:
                print("No companies found with that name.")
                
        elif choice == "4":
            company_id = input("Enter company ID: ")
            if company_id.isdigit():
                company = session.get(Company, int(company_id))
                if company:
                    print(f"\nCompany: {company.name}")
                    print(f"Founded: {company.founding_year}")
                    print("\nCars:")
                    for car in company.cars:
                        print(f" - {car.year} {car.make} {car.model} (KSH {car.price:,})")
                    print("\nCustomers:")
                    for customer in company.customers:
                        print(f" - {customer.name} ({customer.phone})")
                else:
                    print("Company not found.")
            else:
                print("Invalid ID. Please enter a number.")
                
        elif choice == "5":
            company_id = input("Enter company ID to delete: ")
            if company_id.isdigit():
                company = session.get(Company, int(company_id))
                if company:
                    session.delete(company)
                    session.commit()
                    print("Company deleted successfully!")
                else:
                    print("Company not found.")
            else:
                print("Invalid ID. Please enter a number.")
                
        elif choice == "6":
            break
            
        else:
            print("Invalid choice. Please try again.")

def manage_customers():
    while True:
        print("\nCustomer Management")
        print("1. Create Customer")
        print("2. View All Customers")
        print("3. Find Customer by Name")
        print("4. View Customer Details")
        print("5. Delete Customer")
        print("6. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter customer name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            company_id = input("Enter company ID: ")
            
            if company_id.isdigit():
                company = session.get(Company, int(company_id))
                if company:
                    customer = Customer(name=name, phone=phone, email=email, company=company)
                    session.add(customer)
                    session.commit()
                    print(f"Customer {name} created successfully!")
                else:
                    print("Company not found.")
            else:
                print("Invalid company ID. Please enter a number.")
                
        elif choice == "2":
            customers = session.query(Customer).all()
            for customer in customers:
                print(f"{customer.id}: {customer.name} ({customer.phone})")
                
        elif choice == "3":
            name = input("Enter customer name to search: ")
            customers = session.query(Customer).filter(Customer.name.ilike(f"%{name}%")).all()
            if customers:
                for customer in customers:
                    print(f"{customer.id}: {customer.name}")
            else:
                print("No customers found with that name.")
                
        elif choice == "4":
            customer_id = input("Enter customer ID: ")
            if customer_id.isdigit():
                customer = session.get(Customer, int(customer_id))
                if customer:
                    print(f"\nCustomer: {customer.name}")
                    print(f"Phone: {customer.phone}")
                    print(f"Email: {customer.email}")
                    print(f"Company: {customer.company.name}")
                    print("\nCars Purchased:")
                    for car in customer.cars:
                        print(f" - {car.year} {car.make} {car.model} (KSH {car.price:,})")
                else:
                    print("Customer not found.")
            else:
                print("Invalid ID. Please enter a number.")
                
        elif choice == "5":
            customer_id = input("Enter customer ID to delete: ")
            if customer_id.isdigit():
                customer = session.get(Customer, int(customer_id))
                if customer:
                    session.delete(customer)
                    session.commit()
                    print("Customer deleted successfully!")
                else:
                    print("Customer not found.")
            else:
                print("Invalid ID. Please enter a number.")
                
        elif choice == "6":
            break
            
        else:
            print("Invalid choice. Please try again.")

def manage_cars():
    while True:
        print("\nCar Management")
        print("1. Create Car")
        print("2. View All Cars")
        print("3. Find Car by Make/Model")
        print("4. View Car Details")
        print("5. Delete Car")
        print("6. Sell Car to Customer")
        print("7. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            make = input("Enter car make: ")
            model = input("Enter car model: ")
            year = input("Enter year: ")
            price = input("Enter price (KSH): ")
            company_id = input("Enter company ID: ")
            
            if year.isdigit() and price.isdigit() and company_id.isdigit():
                company = session.get(Company, int(company_id))
                if company:
                    car = Car(make=make, model=model, year=int(year), 
                            price=int(price), company=company)
                    session.add(car)
                    session.commit()
                    print(f"Car {make} {model} added successfully!")
                else:
                    print("Company not found.")
            else:
                print("Invalid input. Year, price and company ID must be numbers.")
                
        elif choice == "2":
            cars = session.query(Car).all()
            for car in cars:
                owner = car.customer.name if car.customer else "Available"
                print(f"{car.id}: {car.year} {car.make} {car.model} (KSH {car.price:,}) - {owner}")
                
        elif choice == "3":
            search = input("Enter make or model to search: ")
            cars = session.query(Car).filter(
                (Car.make.ilike(f"%{search}%")) | 
                (Car.model.ilike(f"%{search}%"))
            ).all()
            if cars:
                for car in cars:
                    owner = car.customer.name if car.customer else "Available"
                    print(f"{car.id}: {car.year} {car.make} {car.model} - {owner}")
            else:
                print("No cars found matching your search.")
                
        elif choice == "4":
            car_id = input("Enter car ID: ")
            if car_id.isdigit():
                car = session.get(Car, int(car_id))
                if car:
                    print(f"\nCar Details:")
                    print(f"Make: {car.make}")
                    print(f"Model: {car.model}")
                    print(f"Year: {car.year}")
                    print(f"Price: KSH {car.price:,}")
                    print(f"Company: {car.company.name}")
                    if car.customer:
                        print(f"Owner: {car.customer.name}")
                    else:
                        print("Status: Available for sale")
                else:
                    print("Car not found.")
            else:
                print("Invalid ID. Please enter a number.")
                
        elif choice == "5":
            car_id = input("Enter car ID to delete: ")
            if car_id.isdigit():
                car = session.get(Car, int(car_id))
                if car:
                    session.delete(car)
                    session.commit()
                    print("Car deleted successfully!")
                else:
                    print("Car not found.")
            else:
                print("Invalid ID. Please enter a number.")
                
        elif choice == "6":
            car_id = input("Enter car ID to sell: ")
            customer_id = input("Enter customer ID: ")
            
            if car_id.isdigit() and customer_id.isdigit():
                car = session.get(Car, int(car_id))
                customer = session.get(Customer, int(customer_id))
                
                if car and customer:
                    if car.customer_id:
                        print("This car is already sold!")
                    else:
                        car.customer = customer
                        session.commit()
                        print(f"Car sold to {customer.name} successfully!")
                else:
                    print("Car or customer not found.")
            else:
                print("Invalid IDs. Please enter numbers.")
                
        elif choice == "7":
            break
            
        else:
            print("Invalid choice. Please try again.")

def main():
    try:
        while True:
            display_menu()
            choice = input("Enter your choice: ")
            
            if choice == "1":
                manage_companies()
            elif choice == "2":
                manage_customers()
            elif choice == "3":
                manage_cars()
            elif choice == "4":
                print("Exiting Skiees Motors Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    main()