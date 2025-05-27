from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Owner, Pet, Vaccination

engine = create_engine('sqlite:///vaccine.db')
Session = sessionmaker(bind=engine)
session = Session()

session.query(Vaccination).delete()
session.query(Pet).delete()
session.query(Owner).delete()

o1 = Owner(name="Ali", phone="0712345678")
o2 = Owner(name="Joy", phone="0798765432")

p1 = Pet(name="Max", species="Dog", owner=o1)
p2 = Pet(name="Milo", species="Cat", owner=o2)

v1 = Vaccination(name="Rabies", date="2024-01-10", pet=p1)
v2 = Vaccination(name="Deworming", date="2024-02-20", pet=p1)
v3 = Vaccination(name="Feline Distemper", date="2024-03-15", pet=p2)

session.add_all([o1, o2, p1, p2, v1, v2, v3])
session.commit()
print(" Successful.")
