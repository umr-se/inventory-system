# 📊Inventory System

This project is a FastAPI application that allows syncing data from Google Sheets into a local database and generating reports from the synced data. It uses SQLAlchemy for database interactions and can be run using `uvicorn`.

---

## 🚀 Features

- ✅ Sync Google Sheets to a database
- 📄 Generate reports from the database
- 🔁 RESTful API using FastAPI
- 🛠️ Modular codebase (`db.py`, `sync.py`, `report.py`)

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/umr-se/inventory-system.git
cd inventory-system
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
```
DATABASE_URL=sqlite:///./test.db
GOOGLE_SHEET_ID=your_google_sheet_id
```

### 4. Running the Application
```bash
uvicorn app.main:app --reload
```

![image](https://github.com/user-attachments/assets/15a4621d-7970-4ef9-85bf-d7db8b9fb3d1)
![image](https://github.com/user-attachments/assets/711c14bb-a34c-4cc0-9f77-7337045df558)
![image](https://github.com/user-attachments/assets/533b556c-edac-48d0-b085-789f0b10d699)




