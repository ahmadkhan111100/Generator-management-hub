import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Page configuration
st.set_page_config(page_title="Complaint Workflow Hub", page_icon="📝", layout="centered")

st.title("📋 Complaint Management Workflow")
st.write("Pehle data enter karein, phir review tab mein ja kar data check karke Final Save karein.")

# 1. BACKUP PROFORMA DATA
branch_proforma = {
    "BR-001": "Lahore Main Office",
    "BR-002": "Karachi Saddar Branch",
    "BR-003": "Islamabad Blue Area",
    "BR-004": "Faisalabad Clock Tower",
    "BR-005": "Multan Cantt Branch"
}

project_list = ["Project Alpha", "Project Beta", "Project Delta", "Project Titan"]
team_list = ["Ali Khan", "Zainab Ahmed", "Bilal Siddiqui", "Hamza Usman"]

# Initialize Session State to hold data temporarily before final saving
if "temp_data" not in st.session_state:
    st.session_state.temp_data = None

# Create two tabs: One for Entry, One for Review & Final Save
tab1, tab2 = st.tabs(["📝 1. Data Entry Form", "👀 2. Review & Save"])

# -----------------------------------------------------------------
# TAB 1: DATA ENTRY FORUM
# -----------------------------------------------------------------
with tab1:
    st.subheader("Nayi Complaint Ki Entry Karein")
    
    comp_date = st.date_input("Select Date:", datetime.today(), key="entry_date")
    project = st.selectbox("Select Project Name:", [""] + project_list, key="entry_project")
    b_code = st.selectbox("Select Branch Code:", [""] + list(branch_proforma.keys()), key="entry_bcode")
    
    # Automated Branch Name logic
    b_name = branch_proforma.get(b_code, "")
    st.text_input("Branch Name (Automated):", value=b_name, disabled=True, key="entry_bname")
    
    capacity = st.text_input("Generator Capacity (e.g., 50 KVA):", key="entry_capacity")
    rating = st.text_input("Generator Rating (e.g., Prime / Standby):", key="entry_rating")
    assigned_team = st.selectbox("Assign To (Team Member):", [""] + team_list, key="entry_team")
    remarks = st.text_area("Remarks / Complaint Description:", key="entry_remarks")
    
    # Temporary hold data button
    if st.button("Proceed to Review ➡️"):
        if not (project and b_code and capacity and rating and assigned_team):
            st.error("❌ Galti! Meharbani karke pehle tamam fields fill karein.")
        else:
            # Store data in session memory
            st.session_state.temp_data = {
                "Date": comp_date.strftime("%Y-%m-%d"),
                "Project Name": project,
                "Branch Code": b_code,
                "Branch Name": b_name,
                "Generator Capacity": capacity,
                "Rating": rating,
                "Assigned Team Member": assigned_team,
                "Remarks": remarks
            }
            st.success("✅ Data temporary save ho gaya hai! Ab upar '2. Review & Save' tab par click karein.")

# -----------------------------------------------------------------
# TAB 2: REVIEW AND FINAL SAVE BUTTON
# -----------------------------------------------------------------
with tab2:
    st.subheader("Entered Data Ka Review")
    
    if st.session_state.temp_data is None:
        st.info("ℹ️ Abhi tak koi data enter nahi kiya gaya. Pehle pehle tab mein data enter karein.")
    else:
        data = st.session_state.temp_data
        
        # Display entered data clearly to the user
        st.markdown(f"""
        **Aap ka darj kiya hua data niche mojud hai:**
        * 📅 **Date:** {data['Date']}
        * 📁 **Project Name:** {data['Project Name']}
        * 🔢 **Branch Code:** {data['Branch Code']}
        * 🏢 **Branch Name:** {data['Branch Name']}
        * ⚡ **Generator Capacity:** {data['Generator Capacity']}
        * 📊 **Rating:** {data['Rating']}
        * 👤 **Assigned To:** {data['Assigned Team Member']}
        * 💬 **Remarks:** {data['Remarks'] if data['Remarks'] else 'None'}
        """)
        
        st.markdown("---")
        
        # Final Save Button
        if st.button("💾 Press to Final Save & Send SMS"):
            # Prepare dataframe
            df_new = pd.DataFrame([{
                "Date": data["Date"],
                "Project Name": data["Project Name"],
                "Branch Code": data["Branch Code"],
                "Branch Name": data["Branch Name"],
                "Generator Capacity": data["Generator Capacity"],
                "Rating": data["Rating"],
                "Assigned Team Member": data["Assigned Team Member"],
                "Remarks": data["Remarks"]
            }])
            
            excel_file = "complaints.xlsx"
            
            # Save to Excel
            if os.path.exists(excel_file):
                df_old = pd.read_excel(excel_file)
                df_final = pd.concat([df_old, df_new], ignore_index=True)
            else:
                df_final = df_new
                
            df_final.to_excel(excel_file, index=False)
            
            # Show Success message and SMS Preview
            st.success("🎉 Mubarak ho! Data final Excel file mein save ho chuka hai.")
            
            st.markdown("### 📱 Dispatched SMS Preview")
            st.info(f"""
            **To:** {data['Assigned Team Member']}  
            **Message:** Nayi complaint assign hui hai.  
            * **Branch:** {data['Branch Name']} ({data['Branch Code']})  
            * **Capacity/Rating:** {data['Generator Capacity']} / {data['Rating']}  
            * **Remarks:** {data['Remarks'] if data['Remarks'] else 'None'}
            """)
            
            # Clear memory after saving so form resets
            st.session_state.temp_data = None
