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