import sqlite3
import streamlit as st
from datetime import datetime, timedelta

# --- 1. CORE CONFIGURATION & CONSTANTS ---
DB_NAME = "maintenance_system.db"
STATIONS_LIST = ["Central Area", "North District", "South Coast", "Industrial Zone", "West Suburbs"]

# --- 2. DATABASE SYSTEM LAYOUT ---
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT,
            client_email TEXT,
            city_area TEXT,
            status TEXT,
            assigned_team_member TEXT,
            created_at TEXT,
            dispatched_at TEXT,
            last_reminder_sent TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ledger (
            invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id INTEGER,
            client_name TEXT,
            amount REAL,
            status TEXT,
            outstanding_balance REAL,
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

def trigger_system_email(to_email, subject, body):
    st.toast(f"📧 Email Sent to {to_email}!")
    with st.expander(f"👁️ View Simulated Email: {subject}"):
        st.caption(f"**To:** {to_email}")
        st.text(body)

# --- 3. STREAMLIT APP LAYOUT ---
st.set_page_config(page_title="FSM Generator Ticketing System", layout="wide")
init_db()

st.title("⚙️ Generator Field Service & Automated Ledger Hub")
st.markdown("Fully managed ticketing, escalation pipeline, automated invoicing, and collection reminders.")

st.sidebar.header("🛠️ System Diagnostics")
if st.sidebar.button("⏰ Run Daily Payment Reminders Engine"):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    today = datetime.now().date()
    cursor.execute('''
        SELECT t.ticket_id, t.client_name, t.client_email, t.dispatched_at, t.last_reminder_sent, l.invoice_id, l.outstanding_balance 
        FROM tickets t JOIN ledger l ON t.ticket_id = l.ticket_id WHERE l.status = 'Dispatched' AND l.outstanding_balance > 0
    ''')
    active_debts = cursor.fetchall()
    reminders_sent = 0
    for row in active_debts:
        t_id, name, email, disp_str, last_rem_str, inv_id, balance = row
        if disp_str and last_rem_str:
            disp_date = datetime.strptime(disp_str, '%Y-%m-%d').date()
            last_rem = datetime.strptime(last_rem_str, '%Y-%m-%d').date()
            if (today - disp_date).days >= 10 and (today - last_rem).days >= 2:
                trigger_system_email(email, f"⚠️ Overdue Payment Reminder: Invoice #{inv_id}", f"Dear {name},\nOutstanding Balance: ${balance}.")
                cursor.execute("UPDATE tickets SET last_reminder_sent = ? WHERE ticket_id = ?", (today.strftime('%Y-%m-%d'), t_id))
                reminders_sent += 1
    conn.commit()
    conn.close()
    st.sidebar.success(f"Reminder sweep finished. {reminders_sent} emails processed.")

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()
cursor.execute("SELECT ticket_id, client_name FROM tickets WHERE status = 'Work Completed' AND ticket_id NOT IN (SELECT ticket_id FROM ledger)")
unvoiced = cursor.fetchall()
conn.close()

if unvoiced:
    for item in unvoiced:
        st.sidebar.error(f"⚠️ Missing Invoice Alert: Ticket #{item} for '{item}' completed work but lacks a ledger entry!")

tab1, tab2, tab3 = st.tabs(["🎫 Open Active Tickets", "➕ Log New Complaint", "🧾 Financial Ledgers"])

with tab1:
    st.header("Active Operation Board")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickets ORDER BY ticket_id DESC")
    tickets = cursor.fetchall()
    conn.close()

    if not tickets:
        st.info("No trouble shoot tickets currently registered inside the database.")
    else:
        for t in tickets:
            t_id, name, email, area, status, team_member, created, disp_date, _ = t
            with st.container(border=True):
                col1, col2, col3 = st.columns()
                with col1:
                    st.subheader(f"Ticket #{t_id}")
                    st.caption(f"**Area:** {area}\n\n**Logged:** {created}")
                with col2:
                    st.write(f"**Client:** {name} ({email})")
                    st.markdown(f"**Current Status:** :blue[{status}]")
                    if team_member:
                        st.write(f"**Assigned Field Tech:** {team_member}")
                with col3:
                    if status == "Received":
                        tech = st.text_input("Assign Area Team Member", key=f"tech_{t_id}", placeholder="John Doe")
                        if st.button("🚀 Dispatch Team", key=f"disp_{t_id}") and tech:
                            conn = sqlite3.connect(DB_NAME)
                            cursor = conn.cursor()
                            cursor.execute("UPDATE tickets SET status='Team Dispatched', assigned_team_member=? WHERE ticket_id=?", (tech, t_id))
                            conn.commit()
                            conn.close()
                            trigger_system_email(email, f"Team Dispatched - Ticket #{t_id}", f"Dear {name},\nOur service team member ({tech}) is moving to your branch to analyze the generator.")
                            st.rerun()
                    elif status == "Team Dispatched":
                        scope = st.text_input("Scope of Fault Details", key=f"scope_{t_id}", placeholder="Blown gasket replacement")
                        cost = st.number_input("Quotation Amount ($)", key=f"cost_{t_id}", min_value=0.0)
                        if st.button("📤 Generate & Send Quotation", key=f"quote_{t_id}"):
                            conn = sqlite3.connect(DB_NAME)
                            cursor = conn.cursor()
                            cursor.execute("UPDATE tickets SET status='Quotation Sent' WHERE ticket_id=?", (t_id,))
                            conn.commit()
                            conn.close()
                            trigger_system_email(email, f"Quotation: Generator Fault - Ticket #{t_id}", f"Dear {name},\nOur team found a fault. Scope: {scope}. Estimated Cost: ${cost}. Please send written approval.")
                            st.rerun()
                    elif status == "Quotation Sent":
                        if st.button("✅ Client Approval Received", key=f"appr_{t_id}"):
                            conn = sqlite3.connect(DB_NAME)
                            cursor = conn.cursor()
                            cursor.execute("UPDATE tickets SET status='Approved' WHERE ticket_id=?", (t_id,))
                            conn.commit()
                            conn.close()
                            trigger_system_email(email, f"Approval Acknowledged - Ticket #{t_id}", f"Dear {name},\nApproval received. Our team will reach your branch soon to resolve the generator issue.")
                            st.rerun()
                    elif status == "Approved":
                        amount_final = st.number_input("Final Invoice Amount ($)", key=f"fin_amt_{t_id}", min_value=0.0)
                        if st.button("🏁 Sign Off Work Completion", key=f"comp_{t_id}"):
                            conn = sqlite3.connect(DB_NAME)
                            cursor = conn.cursor()
                            cursor.execute("UPDATE tickets SET status='Work Completed' WHERE ticket_id=?", (t_id,))
                            now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            cursor.execute("INSERT INTO ledger (ticket_id, client_name, amount, status, outstanding_balance, created_at) VALUES (?, ?, ?, 'Ready for Submission', ?, ?)", (t_id, name, amount_final, amount_final, now_str))
                            conn.commit()
                            conn.close()
                            trigger_system_email(email, f"Work Completed Report - Ticket #{t_id}", f"Dear {name},\nWork completed. Your generator has been started and is in a working position.")
                            trigger_system_email(email, f"Invoice Pending - Ticket #{t_id}", f"Dear {name},\nYour invoice is ready and waiting for dispatch verification.")
                            st.rerun()
                    else:
                        st.write("🟢 Workflow Completed")

with tab2:
    st.header("Log Incoming Trouble Shoot Ticket")
    with st.form("intake_form", clear_on_submit=True):
        c_name = st.text_input("Client/Branch Corporation Name")
        c_email = st.text_input("Client Communication Email Address")
        c_area = st.selectbox("Concerns City Area Team Assignment Location", STATIONS_LIST)
if st.form_submit_button("Register System Ticket"):
            if c_name and c_email:
                conn = sqlite3.connect(DB_NAME)
                cursor = conn.cursor()
                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute("INSERT INTO tickets (client_name, client_email, city_area, status, created_at) VALUES (?, ?, ?, 'Received', ?)", (c_name, c_email, c_area, now))
                t_idx = cursor.lastrowid
                conn.commit()
                conn.close()
                trigger_system_email(c_email, f"Complaint Registered - Ticket #{t_idx}", f"Dear {c_name},\nYour ticket has been logged for {c_area}.")
                st.success(f"Ticket #{t_idx} created successfully.")
            else:
                st.error("Please fill out all missing corporate metadata text-fields.")

with tab3:
    st.header("Financial Tracking & Accounts Receivables Ledger")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ledger ORDER BY invoice_id DESC")
    ledgers = cursor.fetchall()
    conn.close()

if not ledgers:
    st.info("No recorded ledger transactions currently found.")
else:
    for l in ledgers:
        if status == "Paid":
            pass 
        elif status in ["Dispatched", "Partially Paid"] and balance > 0:
            payment = st.number_input("Record Incoming Collection ($)", max_value=float(balance), min_value=0.0, key=f"pay_in_{inv_id}")
            if st.button("💰 Log Payment", key=f"log_pay_{inv_id}"):
                conn = sqlite3.connect(DB_NAME)
                cursor = conn.cursor()
                new_bal = float(balance) - payment
                new_stat = "Paid" if new_bal <= 0 else "Partially Paid"
                cursor.execute("UPDATE ledger SET outstanding_balance=?, status=? WHERE invoice_id=?", (new_bal, new_stat, inv_id))
                conn.commit()
                conn.close()
                st.success(f"Logged payment of ${payment}.")
                st.rerun()




