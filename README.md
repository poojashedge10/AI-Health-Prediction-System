# AI-Health-Prediction-System
AI Health Prediction System  A professional healthcare prediction application developed using Python, Streamlit, Machine Learning, and MySQL.
# AI Health Prediction System

A professional healthcare prediction application developed using Python, Streamlit, Machine Learning, and MySQL.

---

# Project Overview

The AI Health Prediction System is designed to manage patient health records and predict possible health risks based on blood test values such as glucose, haemoglobin, and cholesterol levels.

The application provides CRUD operations, machine learning-based prediction, input validation, and database management using MySQL.

This project was developed as part of an AI/ML technical assessment to demonstrate practical implementation of:

* Python Development
* Machine Learning
* Database Integration
* Streamlit Web Application Development
* Predictive Analytics

---

# Features

* Add Patient Records
* View Patient Records
* Delete Patient Records
* Machine Learning-Based Health Risk Prediction
* Input Validation
* MySQL Database Integration
* Streamlit User Interface
* Real-Time Prediction Result
* Persistent Data Storage

---

# Technologies Used

## Frontend

* Streamlit

## Backend

* Python

## Database

* MySQL

## Machine Learning

* Scikit-learn
* Random Forest Classifier

## Libraries

* Pandas
* NumPy
* Joblib
* Matplotlib
* mysql-connector-python

---

# Machine Learning Model

The project uses a Random Forest Classifier trained on a healthcare dataset to predict health risk categories.

### Input Features

* Blood Glucose Level
* Haemoglobin Level
* Cholesterol Level

### Prediction Categories

* Low Risk
* Moderate Risk
* High Risk

---

# Project Structure

```bash
health-prediction-app/
│
├── app.py
├── database.py
├── train_model.py
├── requirements.txt
├── dataset.csv
├── model.pkl
├── README.md
│
└── screenshots/
```

---

# Installation Steps

## Step 1 — Clone Repository

```bash
git clone <repository-link>
```

## Step 2 — Install Required Libraries

```bash
pip install -r requirements.txt
```

## Step 3 — Configure MySQL Database

Create database:

```sql
CREATE DATABASE health_prediction_db;
```

Create table:

```sql
CREATE TABLE patients (
    id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100),
    dob DATE,
    email VARCHAR(100),
    glucose FLOAT,
    haemoglobin FLOAT,
    cholesterol FLOAT,
    remarks VARCHAR(255)
);
```

## Step 4 — Run Model Training

```bash
python train_model.py
```

## Step 5 — Run Streamlit Application

```bash
streamlit run app.py
```

---

# Validation Features

The application validates:

* Email format
* Numeric medical values
* Required patient information
* Valid date input

---

# Prediction Logic

The system predicts health risk using medical test values:

* High glucose or cholesterol values → High Risk
* Moderate values → Moderate Risk
* Normal values → Low Risk

---

# Screenshots

Add screenshots inside the screenshots folder.

Example:

* Dashboard
* Add Patient Page
* View Records Page
* Prediction Result

---

# Future Improvements

* User Authentication System
* Advanced AI Prediction Models
* Cloud Deployment
* Patient Report Generation
* Data Visualization Dashboard
* REST API Integration

---

# Author

Pooja Dilip Shedge

* B.Sc Computer Science Graduate
* Data Science Intern
* AI/ML Enthusiast

---

# Conclusion

This project demonstrates practical implementation of machine learning, healthcare prediction systems, database management, and full-stack Python application development using Streamlit and MySQL.
