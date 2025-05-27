# Vet Vaccination CLI Project

This is a terminal-based Python application that helps track pet owners, their pets, and vaccinations using SQLite and SQLAlchemy.

---

## 📌 Project Description

The Vet Vaccination CLI is built to help veterinarians or clinics manage vaccination records.  
It keeps track of:
- Owners (name and contact)
- Pets (name, species, and their owner)
- Vaccinations (name, date, and which pet it belongs to)

The project uses a simple command-line interface to interact with a local SQLite database.

---

## 🧰 Tech Stack

- Python 3.8+
- SQLite (local database)
- SQLAlchemy (ORM)
- CLI (Command-Line Interface)

---

## 🗃️ Database Models

### Owner Table

| Field | Type | Description       |
|-------|------|-------------------|
| id    | int  | Primary Key       |
| name  | str  | Owner's name      |
| phone | str  | Contact number    |

### Pet Table

| Field     | Type | Description              |
|-----------|------|--------------------------|
| id        | int  | Primary Key              |
| name      | str  | Pet's name               |
| species   | str  | Pet species (e.g., dog)  |
| owner_id  | int  | Foreign Key to Owner     |

### Vaccination Table

| Field    | Type | Description              |
|----------|------|--------------------------|
| id       | int  | Primary Key              |
| name     | str  | Vaccine name             |
| date     | str  | Date given (YYYY-MM-DD)  |
| pet_id   | int  | Foreign Key to Pet       |

---

## 🔁 Relationships

- One Owner → Many Pets  
- One Pet → Many Vaccinations

---

## 💡 User Stories

- As a user, I can view all owners, pets, and vaccinations
- I can add a new owner, pet, or vaccination
- I can navigate the system through a CLI
- All data is saved to a SQLite database

---

## 🚀 How to Run

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Create the database
python create_db.py

# Step 3: Seed initial data 
python -m app.seed

# Step 4: Start the CLI app
python -m app.cli
