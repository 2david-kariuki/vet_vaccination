from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Owner, Pet, Vaccination


engine = create_engine('sqlite:///vaccine.db')
Session = sessionmaker(bind=engine)
session = Session()


def menu():
    while True:
        print("\nVet Vaccination Tracker")
        print("1. View all owners")
        print("2. View all pets")
        print("3. View all vaccinations")
        print("4. Add a new owner")
        print("5. Add a new pet")
        print("6. Add a new vaccination")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            view_owners()
        elif choice == "2":
            view_pets()
        elif choice == "3":
            view_vaccinations()
        elif choice == "4":
            add_owner()
        elif choice == "5":
            add_pet()
        elif choice == "6":
            add_vaccination()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 7.")

def view_owners():
    owners = session.query(Owner).all()
    for owner in owners:
        print(f"{owner.id} | {owner.name} | {owner.phone}")


def view_pets():
    pets = session.query(Pet).all()
    for pet in pets:
        print(f"{pet.id} | {pet.name} | {pet.species} | Owner ID: {pet.owner_id}")


def view_vaccinations():
    vaccinations = session.query(Vaccination).all()
    for v in vaccinations:
        print(f"{v.id} | {v.name} on {v.date} | Pet ID: {v.pet_id}")


def add_owner():
    name = input("Enter owner name: ")
    phone = input("Enter phone number: ")
    if name and phone:
        session.add(Owner(name=name, phone=phone))
        session.commit()
        print("Owner added.")
    else:
        print("Missing information.")


def add_pet():
    name = input("Enter pet name: ")
    species = input("Enter species: ")
    owner_id = input("Enter owner ID: ")
    if name and species and owner_id.isdigit():
        session.add(Pet(name=name, species=species, owner_id=int(owner_id)))
        session.commit()
        print("Pet added.")
    else:
        print("Invalid input.")


def add_vaccination():
    name = input("Enter vaccine name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    pet_id = input("Enter pet ID: ")
    if name and date and pet_id.isdigit():
        session.add(Vaccination(name=name, date=date, pet_id=int(pet_id)))
        session.commit()
        print("Vaccination added.")
    else:
        print("Invalid input.")


if __name__ == "__main__":
    menu()
