# ============================================================
# F&A ENTERPRISES
# Generator Operations Management System (GOMS)
# app.py
# Part 1A-1
# ============================================================

import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
import plotly.express as px

# -----------------------------
# Streamlit Page Configuration
# -----------------------------
st.set_page_config(
    page_title="F&A Generator Management System",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background:#f4f6f9;
}

.block-container{
    padding-top:1rem;
}

h1,h2,h3{
    color:#003366;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:10px;
    padding:15px;
    box-shadow:0px 2px 8px rgba(0,0,0,.15);
}

.stButton>button{
    width:100%;
    background:#003366;
    color:white;
    border-radius:8px;
}

.stButton>button:hover{
    background:#ff6600;
    color:white;
}

.sidebar .sidebar-content{
    background:#002147;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Database
# -----------------------------
conn = sqlite3.connect(
    "generator_management.db",
    check_same_thread=False
)

cur = conn.cursor()

# -----------------------------
# Create Tables
# -----------------------------
cur.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE,
password TEXT,
role TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS branches(
id INTEGER PRIMARY KEY AUTOINCREMENT,
branch_name TEXT,
city TEXT,
address TEXT,
contact_person TEXT,
phone TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS generators(
id INTEGER PRIMARY KEY AUTOINCREMENT,
generator_code TEXT,
capacity TEXT,
brand TEXT,
model TEXT,
branch TEXT,
status TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS complaints(
id INTEGER PRIMARY KEY AUTOINCREMENT,
complaint_no TEXT,
branch TEXT,
generator TEXT,
description TEXT,
priority TEXT,
status TEXT,
created_date TEXT
)
""")

conn.commit()

# -----------------------------
# Default Admin User
# -----------------------------
cur.execute("SELECT * FROM users WHERE username='admin'")

if cur.fetchone() is None:
    cur.execute("""
        INSERT INTO users
        (username,password,role)
        VALUES
        ('admin','admin123','Administrator')
    """)
    conn.commit()

# -----------------------------
# Login Session
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "role" not in st.session_state:
    st.session_state.role = ""

# -----------------------------
# Login Screen
# -----------------------------
def login():

    st.title("⚡ F&A Enterprises")

    st.subheader("Generator Operations Management System")

    st.write("Please login to continue")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        cur.execute("""
        SELECT * FROM users
        WHERE username=?
        AND password=?
        """,(username,password))

        user = cur.fetchone()

        if user:

            st.session_state.logged_in = True
            st.session_state.username = user[1]
            st.session_state.role = user[3]

            st.rerun()

        else:

            st.error("Invalid Username or Password")
