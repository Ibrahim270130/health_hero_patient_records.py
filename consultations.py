def get_patient_consultations(patient_id):
    conn = sqlite3.connect("health_hero.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.consultation_date, d.name AS doctor_name, c.notes
        FROM Consultations c
        JOIN Doctors d ON c.doctor_id = d.doctor_id
        WHERE c.patient_id = ?
    """, (patient_id,))
    results = cursor.fetchall()
    conn.close()
    return results

# Example: Fetch consultations for patient with ID 1
consultations = get_patient_consultations(1)
for c in consultations:
    print(f"Date: {c[0]}, Doctor: {c[1]}, Notes: {c[2]}")
