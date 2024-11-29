def add_patient(name, age, gender, contact_info):
    conn = sqlite3.connect("health_hero.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Patients (name, age, gender, contact_info) VALUES (?, ?, ?, ?)", 
                   (name, age, gender, contact_info))
    conn.commit()
    conn.close()

# Example: Add a patient
add_patient("John Doe", 30, "Male", "555-1234")
print("Patient added successfully!")
