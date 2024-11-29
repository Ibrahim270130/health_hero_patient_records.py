import sqlite3

# Connect to SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect("health_hero.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    contact_info TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Doctors (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialty TEXT NOT NULL,
    contact_info TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Consultations (
    consultation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    consultation_date DATE NOT NULL,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Diagnoses (
    diagnosis_id INTEGER PRIMARY KEY AUTOINCREMENT,
    consultation_id INTEGER NOT NULL,
    diagnosis TEXT NOT NULL,
    FOREIGN KEY (consultation_id) REFERENCES Consultations(consultation_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Medications (
    medication_id INTEGER PRIMARY KEY AUTOINCREMENT,
    consultation_id INTEGER NOT NULL,
    medication_name TEXT NOT NULL,
    dosage TEXT NOT NULL,
    FOREIGN KEY (consultation_id) REFERENCES Consultations(consultation_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS TreatmentPlans (
    treatment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    plan_details TEXT NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
)
""")

# Commit changes and close the connection
conn.commit()
conn.close()
print("Database and tables created successfully!")
