import streamlit as st
import pandas as pd
import mysql.connector
import joblib
import re

from database import connect_db

model = joblib.load("model.pkl")

st.set_page_config(page_title="AI Health Prediction System")

st.title("AI Health Prediction System")

menu = [
    "Add Patient",
    "View Patients",
    "Delete Patient"
]

choice = st.sidebar.selectbox("Navigation", menu)

def validate_email(email):

    email = email.strip()

    if "@" in email and "." in email:
        return True

    return False

def predict_risk(glucose, haemoglobin, cholesterol):

    if glucose > 180 or cholesterol > 240:
        return "High Risk"

    elif glucose > 120:
        return "Moderate Risk"

    else:
        return "Low Risk"

# ADD PATIENT

if choice == "Add Patient":

    st.subheader("Add Patient")

    full_name = st.text_input("Full Name")

    dob = st.date_input("Date of Birth")

    email = st.text_input("Email")

    glucose = st.number_input("Glucose")

    haemoglobin = st.number_input("Haemoglobin")

    cholesterol = st.number_input("Cholesterol")

    if st.button("Submit"):

        if not validate_email(email):

            st.error("Invalid Email")

        else:

            remarks = predict_risk(
                glucose,
                haemoglobin,
                cholesterol
            )

            conn = connect_db()

            cursor = conn.cursor()

            query = '''
            INSERT INTO patients
            (
                full_name,
                dob,
                email,
                glucose,
                haemoglobin,
                cholesterol,
                remarks
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s)
            '''

            values = (
                full_name,
                dob,
                email,
                glucose,
                haemoglobin,
                cholesterol,
                remarks
            )

            cursor.execute(query, values)

            conn.commit()

            conn.close()

            st.success("Patient Added Successfully")

            st.info(f"Prediction Result: {remarks}")

# VIEW PATIENTS

elif choice == "View Patients":

    st.subheader("Patient Records")

    conn = connect_db()

    query = "SELECT * FROM patients"

    df = pd.read_sql(query, conn)

    st.dataframe(df)

    conn.close()

# DELETE PATIENT

elif choice == "Delete Patient":

    st.subheader("Delete Patient")

    patient_id = st.number_input(
        "Enter Patient ID",
        min_value=1
    )

    if st.button("Delete"):

        conn = connect_db()

        cursor = conn.cursor()

        query = "DELETE FROM patients WHERE id=%s"

        cursor.execute(query, (patient_id,))

        conn.commit()

        conn.close()

        st.success("Patient Deleted Successfully")