# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Налаштування двигуна
engine = create_engine('postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/postgres')

# Налаштування сесії
Session = sessionmaker(bind=engine)
