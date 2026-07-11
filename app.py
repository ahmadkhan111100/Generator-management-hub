import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Page Configuration
st.set_page_config(page_title="Complaint Management Hub", page_icon="⚙️", layout="centered")

# Title
st.title("⚙️ Complaint Registration Form")
st.write("Meharbani karke complaint ki tafseelat darj karein.")

# 1. Backup Proforma Data (Branch Codes & Names)
branch_proforma = {
    "BR-001": "Lahore Main Office",
    "BR-002": "Karachi Saddar Branch",
    "BR-003": "Islamabad Blue Area",
    "BR-004": "Faisalabad Clock Tower",
    "BR-005": "Multan Cantt Branch"
}

projects = ["Project Alpha", "Project Beta", "Project Delta", "Project Titan"]
team_members = ["Ali Khan", "Zainab Ahmed", "Bilal Siddiqui", "Hamza Usman"]

# ---- INPUT FORM ----
with st.form("complaint_form", clear_on_submit=True):
    
    # Date Input (Calendar built-in in Streamlit)
    comp_date = st.date_input("Select Date:", datetime.today())
    
    # Project Name Dropdown
    project = st.selectbox("Project Name:", [""] + projects)
    
    # Branch Code Dropdown
    b_code = st.selectbox("Branch Code:", [""] + list(branch_proforma.keys()))
    
    # Automated Branch Name logic
    b_name = branch_proforma.get(b_code, "")
    st.text_input("Branch Name (Automated):", value=b_name, disabled=True)
    
    # Generator Details
    capacity = st.text_input("Generator Capacity:")
    rating = st.text_input("Generator Rating:")
    
    # Assigned Team Member Dropdown
    assigned_team = st.selectbox("Assign Team Member:", [""] + team_members)
    
    # Remarks
    remarks = st.text_area("Remarks:")
    
    # Submit Button
    submitted = st.form_submit_button("Submit & Send SMS Alert")

# ---- ACTIONS ON SUBMIT ----
if submitted:
    if not (project and b_code and capacity and rating and assigned_team):
        st.error("❌ Meharbani karke tamam zaroori fields fill karein!")
    else:
        # Data structure for saving
        new_data = {
            "Date": [comp_date.strftime("%Y-%m-%d")],
            "Project Name": [project],
            "Branch Code": [b_code],
            "Branch Name": [b_name],
            "Generator Capacity": [capacity],
            "Rating": [rating],
            "Assigned To": [assigned_team],
            "Remarks": [remarks]
        }
        df_new = pd.DataFrame(new_data)
        excel_file = "complaints.xlsx"
        
        # Save to Excel logic
        if os.path.exists(excel_file):
            df_old = pd.read_excel(excel_file)
            df_final = pd.concat([df_old, df_new], ignore_index=True)
        else:
            df_final = df_new
            
        df_final.to_excel(excel_file, index=False)
