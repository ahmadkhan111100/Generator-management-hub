# ============================================================
# PART 1A-2
# Sidebar, Dashboard & Navigation
# ============================================================

# -----------------------------
# Dashboard Function
# -----------------------------
def dashboard():

    st.title("🏠 Dashboard")

    st.write(
        f"Welcome **{st.session_state.username}** "
        f"({st.session_state.role})"
    )

    # -------------------------
    # Statistics
    # -------------------------
    total_branches = cur.execute(
        "SELECT COUNT(*) FROM branches"
    ).fetchone()[0]

    total_generators = cur.execute(
        "SELECT COUNT(*) FROM generators"
    ).fetchone()[0]

    total_complaints = cur.execute(
        "SELECT COUNT(*) FROM complaints"
    ).fetchone()[0]

    open_jobs = cur.execute("""
        SELECT COUNT(*)
        FROM complaints
        WHERE status='Open'
    """).fetchone()[0]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🏢 Branches",
        total_branches
    )

    col2.metric(
        "⚡ Generators",
        total_generators
    )

    col3.metric(
        "📋 Complaints",
        total_complaints
    )

    col4.metric(
        "🔧 Open Jobs",
        open_jobs
    )

    st.divider()

    # -------------------------
    # Complaint Status Chart
    # -------------------------
    df = pd.read_sql_query("""
        SELECT
        status,
        COUNT(*) total
        FROM complaints
        GROUP BY status
    """, conn)

    if len(df):

        fig = px.pie(
            df,
            values="total",
            names="status",
            title="Complaint Status"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info("No complaint data available.")

    st.divider()

    st.subheader("Latest Complaints")

    recent = pd.read_sql_query("""
        SELECT
        complaint_no,
        branch,
        priority,
        status,
        created_date
        FROM complaints
        ORDER BY id DESC
        LIMIT 10
    """, conn)

    st.dataframe(
        recent,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# Sidebar Navigation
# ============================================================

def sidebar():

    with st.sidebar:

        st.image(
            "https://placehold.co/300x120?text=F%26A+Enterprises",
            use_container_width=True
        )

        st.markdown("## F&A Enterprises")

        st.caption(
            "Generator Operations Management System"
        )

        st.write("---")

        menu = st.radio(
            "Navigation",
            [
                "Dashboard",
                "Branches",
                "Generators",
                "Complaints",
                "Teams",
                "Inventory",
                "Invoices",
                "Finance",
                "Reports",
                "Settings"
            ]
        )

        st.write("---")

        st.success(
            f"User : {st.session_state.username}"
        )

        st.info(
            f"Role : {st.session_state.role}"
        )

        if st.button("🚪 Logout"):

            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.role = ""

            st.rerun()

    return menu


# ============================================================
# Main Application
# ============================================================

if not st.session_state.logged_in:

    login()

else:

    selected = sidebar()

    if selected == "Dashboard":

        dashboard()

    elif selected == "Branches":

        st.header("🏢 Branch Management")
        st.info("Module coming in Part 2")

    elif selected == "Generators":

        st.header("⚡ Generator Management")
        st.info("Module coming in Part 2")

    elif selected == "Complaints":

        st.header("📋 Complaint Management")
        st.info("Module coming in Part 2")

    elif selected == "Teams":

        st.header("👷 Team Management")
        st.info("Module coming in Part 3")

    elif selected == "Inventory":

        st.header("📦 Spare Parts Inventory")
        st.info("Module coming in Part 3")

    elif selected == "Invoices":

        st.header("💰 Invoice Management")
        st.info("Module coming in Part 4")

    elif selected == "Finance":

        st.header("📊 Finance Dashboard")
        st.info("Module coming in Part 4")

    elif selected == "Reports":

        st.header("📑 Reports")
        st.info("Module coming in Part 5")

    elif selected == "Settings":

        st.header("⚙ Settings")
        st.info("Module coming in Part 5")# ============================================================
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
