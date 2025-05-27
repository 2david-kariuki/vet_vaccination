from sqlalchemy import create_engine
from app.models import Base

engine = create_engine('sqlite:///vaccine.db')
Base.metadata.create_all(engine)
print("Successful!")
