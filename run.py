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