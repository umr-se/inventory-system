from .db import Base, engine, SessionLocal

# Initialize database
def init_db():
    Base.metadata.create_all(bind=engine)
    
__version__ = "1.0"
__project__ = "inventory"
__author__ = "umer"