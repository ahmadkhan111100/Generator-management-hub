import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="F&A Generator Management System",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)
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
st.error("Invalid Username or Password")
