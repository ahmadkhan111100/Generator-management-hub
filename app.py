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
    # 1. Main Tickets Table
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
    # 2. Main Ledger Table
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
    # 3. New Clients Profiles Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            client_id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT UNIQUE,
            contact_email TEXT,
            assigned_region TEXT
        )
    ''')
    # 4. New Inventory Tracking Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS parts (
            part_id INTEGER PRIMARY KEY AUTOINCREMENT,
            part_name TEXT UNIQUE,
            unit_price REAL,
            quantity_in_stock INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def trigger_system_email(to_email, subject, body):
    if isinstance(to_email, tuple) and len(to_email) > 0:
        to_email = to_email[0]
    clean_email = str(to_email).strip() if to_email else "unknown_client@system.local"
    
    st.toast(f"📧 Email Sent to {clean_email}!")
    with st.expander(f"👁️ View Simulated Email: {subject}"):
        st.caption(f"**To:** {clean_email}")
        st.text(body)

# --- 3. STREAMLIT APP LAYOUT & NAVIGATION CONFIG ---
st.set_page_config(page_title="FSM Generator Ticketing System", layout="wide")
init_db()

st.title("⚙️ Zubair Enterprises Automated Operation")
st.markdown("Fully managed ticketing, escalation pipeline, automated invoicing, inventory checks, and reminders.")

# Sidebar diagnostics section
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
        st.sidebar.error(f"⚠️ Missing Invoice Alert: Ticket #{item[0]} for '{item[1]}' completed work but lacks a ledger entry!")

# Set up routing tracking system variables
if "selected_tab_index" not in st.session_state:
    st.session_state.selected_tab_index = 0

# Master definitions array containing all tabs
tab_titles = ["🎫 Open Active Tickets", "➕ Log New Complaint", "🧾 Financial Ledgers", "⚙️ Hub Settings"]
tabs = st.tabs(tab_titles)

# --- TAB 1: OPERATIONS SYSTEM BOARD ---
with tabs[0]:
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
                col1, col2, col3 = st.columns(3)
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
                        # Fetch parts to dynamically calculate amounts inside the ticket
                        conn = sqlite3.connect(DB_NAME)
                        cursor = conn.cursor()
                        cursor.execute("SELECT part_name, unit_price, quantity_in_stock FROM parts WHERE quantity_in_stock > 0")
                        avail_parts = cursor.fetchall()
                        conn.close()
                        
                        base_labor = st.number_input("Base Service / Labor Fee ($)", min_value=0.0, step=10.0, value=100.0, key=f"lab_{t_id}")
                        
                        if avail_parts:
                            part_map = {r[0]: {"price": r[1], "stock": r[2]} for r in avail_parts}
                            chosen_part = st.selectbox("Select Part Replaced (Optional)", ["None"] + list(part_map.keys()), key=f"p_sel_{t_id}")
                            if chosen_part != "None":
                                max_stock = int(part_map[chosen_part]["stock"])
                                qty_used = st.number_input(f"Quantity (Max Available: {max_stock})", min_value=1, max_value=max_stock, value=1, step=1, key=f"p_qty_{t_id}")
                                parts_cost = part_map[chosen_part]["price"] * qty_used
                                st.caption(f"🔧 Parts Cost Breakdown: {qty_used} x ${part_map[chosen_part]['price']} = ${parts_cost:,.2f}")
                            else:
                                qty_used = 0
                                parts_cost = 0.0
                        else:
                            st.caption("ℹ️ Internal parts inventory empty. Flat rate processing engine activated.")
                            chosen_part = "None"
                            qty_used = 0
                            parts_cost = 0.0
                                st.markdown("---")
    if st.button("➡️ View Financial Ledgers Panel", key="nav_to_tab3"):
        st.info("Please click '🧾 Financial Ledgers' at the top of the dashboard to continue.")
    st.markdown("---")
    if st.button("➡️ Proceed to Log Complaint Form", key="nav_to_tab2"):
        st.info("Please manually select the next tab above to proceed.")
import sqlite3
import streamlit as st
from datetime import datetime

DB_NAME = "maintenance_system.db"

def init_ledger_db():
    """Initializes the database ledger schema if it does not exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
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

def render_financial_ledger():
    """Renders the dashboard UI and logic for the financial ledger."""
    st.header("🧾 Financial Ledgers & Processing Hub")
    init_ledger_db()

    # --- Ledger Overview Metrics ---
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(amount) FROM ledger")
    total_invoiced = cursor.fetchone()[0] or 0.0
    
    cursor.execute("SELECT SUM(outstanding_balance) FROM ledger")
    total_outstanding = cursor.fetchone()[0] or 0.0
    
    conn.close()
    
    total_collected = total_invoiced - total_outstanding

    metric_col1, metric_col2, metric_col3 = st.columns(3)
    with metric_col1:
        st.metric("Total Invoiced", f"${total_invoiced:,.2f}")
    with metric_col2:
        st.metric("Total Collected", f"${total_collected:,.2f}", delta_color="normal")
    with metric_col3:
        st.metric("Total Outstanding", f"${total_outstanding:,.2f}", delta="-Remaining")

    st.markdown("---")

    # --- Filtering and Queries ---
    filter_status = st.selectbox(
        "Filter Transactions By Status", 
        ["All Records", "Ready for Submission", "Dispatched", "Partially Paid", "Paid"]
    )

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    if filter_status == "All Records":
        cursor.execute("SELECT * FROM ledger ORDER BY invoice_id DESC")
    else:
        cursor.execute("SELECT * FROM ledger WHERE status=? ORDER BY invoice_id DESC", (filter_status,))
        
    ledgers = cursor.fetchall()
    conn.close()

    # --- Data Rendering Loop ---
    if not ledgers:
        st.info(f"No recorded ledger transactions currently found matching: **{filter_status}**")
    else:
        for row in ledgers:
            inv_id, ticket_id, client_name, amount, status, balance, created_at = row
            
            with st.container(border=True):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.subheader(f"Invoice #{inv_id}")
                    st.caption(f"**Associated Ticket:** #{ticket_id}")
                    st.caption(f"**Generated On:** {created_at}")
                    
                with col2:
                    st.write(f"**Client Profile:** {client_name}")
                    st.write(f"**Gross Amount:** ${amount:,.2f}")
                    st.write(f"**Outstanding Balance:** ${balance:,.2f}")
                    
                    if status == "Paid":
                        st.markdown("**Payment Status:** :green[Paid]")
                    elif status in ["Dispatched", "Partially Paid"]:
                        st.markdown(f"**Payment Status:** :orange[{status}]")
                    else:
                        st.markdown(f"**Payment Status:** :red[{status}]")
                        
                with col3:
                    # Context Action A: Dispatching Initial Invoice
                    if status == "Ready for Submission":
                        if st.button("📨 Dispatch Invoice to Client", key=f"disp_inv_{inv_id}"):
                            conn = sqlite3.connect(DB_NAME)
                            cursor = conn.cursor()
                            today_str = datetime.now().strftime('%Y-%m-%d')
                            cursor.execute("UPDATE ledger SET status='Dispatched' WHERE invoice_id=?", (inv_id,))
                            cursor.execute("UPDATE tickets SET dispatched_at=? WHERE ticket_id=?", (today_str, ticket_id))
                            conn.commit()
                            conn.close()
                            
                            st.toast(f"Invoice #{inv_id} successfully marked as dispatched!")
                            st.rerun()
                            
                    # Context Action B: Log incoming collection payments
                    elif status in ["Dispatched", "Partially Paid"] and balance > 0:
                        payment = st.number_input(
                            "Record Incoming Collection ($)", 
                            max_value=float(balance), 
                            min_value=0.0, 
                            step=50.0,
                            key=f"pay_in_{inv_id}"
                        )
                        
                        if st.button("💰 Log Payment", key=f"log_pay_{inv_id}"):
                            if payment > 0:
                                conn = sqlite3.connect(DB_NAME)
                                cursor = conn.cursor()
                                new_bal = float(balance) - payment
                                new_stat = "Paid" if new_bal <= 0 else "Partially Paid"
                                
                                cursor.execute(
                                    "UPDATE ledger SET outstanding_balance=?, status=? WHERE invoice_id=?", 
                                    (new_bal, new_stat, inv_id)
                                )
                                conn.commit()
                                conn.close()
                                
                                st.success(f"Successfully processed collection payment of ${payment:,.2f}!")
                                st.rerun()
                            else:
                                st.error("Collection record amount must be higher than $0.00")
                    else:
                        st.write("🔒 *No manual actions pending for this ledger item.*")

# Standalone runner logic for direct test executions
if __name__ == "__main__":
    st.set_page_config(page_title="Financial Ledger Test Shell", layout="wide")
    render_financial_ledger()

