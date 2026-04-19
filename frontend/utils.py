import streamlit as st
import requests
from config import API_URL
#Common REST API - POST / GET / PUT / PATCH / DELETE
# -----------------------------
# Upload CSV
# -----------------------------
def upload_csv(file):
    # REST API - POST
    return requests.post(
        f"{API_URL}/upload",
        files={"file": file}
    )
# It will call backend - REST API  - URL End Point
# -----------------------------
# Get Students
# -----------------------------
def get_students():
    #REST API - GET
    return requests.get(f"{API_URL}/students")

# -----------------------------
# Add Student
# -----------------------------
def add_student(data):
    # REST API - POST
    return requests.post(f"{API_URL}/students", json=data)

# -----------------------------
# Update Student
# -----------------------------
def update_student(student_id, data):
    return requests.put(f"{API_URL}/students/{student_id}", json=data)

# -----------------------------
# Analytics
# -----------------------------
def get_analytics():
    st.info(" Before Calling BackEnd")
    return requests.get(f"{API_URL}/analytics")

# -----------------------------
# AI Insights
# -----------------------------
def get_ai_insights():
    return requests.get(f"{API_URL}/ai-insights")
