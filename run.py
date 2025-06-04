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
        