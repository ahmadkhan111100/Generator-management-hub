import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Page layout configuration
st.set_page_config(page_title="Data Entry Forum", page_icon="📝", layout="centered")

# Main Title
st.title("📋 Data Entry Forum")
st.write("Enter the required details below and click 'Save Entry'.")

# 1. BACKUP PROFORMA (Data source for automated branch names)
branch_proforma = {
    "BR-001": "Lahore Main Office",
    "BR-002": "Karachi Saddar Branch",
    "BR-003": "Islamabad Blue Area",
    "BR-004": "Faisalabad Clock Tower",
    "BR-005": "Multan Cantt Branch"
}

project_list = ["Project Alpha", "Project Beta", "Project Delta", "Project Titan"]
team_list = ["Ali Khan", "Zainab Ahmed", "Bilal Siddiqui", "Hamza Usman"]

# -----------------------------------------------------------------
# 🧱 EMPTY INPUT FORM
# -----------------------------------------------------------------
# clear_on_submit=True se data save hote hi form dobara khali ho jaye ga
with st.form("empty_entry_form", clear_on_submit=True):
    
    # 1. Date Field (With Calendar Dropdown)
    comp_date = st.date_input("Select Date:", datetime.today())
    
    # 2. Project Name Selection
    project = st.selectbox("Select Project Name:", [""] + project_list)
    
    # 3. Branch Code Selection
    b_code = st.selectbox("Select Branch Code:", [""] + list(branch_proforma.keys()))
    
    # Automated Branch Name (Fetches automatically when Branch Code is selected)
    b_name = branch_proforma.get(b_code, "")
    st.text_input("Branch Name (Automated):", value=b_name, disabled=True)
    
    # 4. Generator Technical Details
    capacity = st.text_input("Generator Capacity (e.g., 50 KVA):")
    rating = st.text_input("Generator Rating (e.g., Prime / Standby):")
    
    # 5. Team Member Assignment
    assigned_team = st.selectbox("Assign To (Team Member):", [""] + team_list)
    
    # 6. Remarks / Complaint Details
    remarks = st.text_area("Remarks / Complaint Description:")
    
    # Submit Button
    submitted = st.form_submit_button("💾 Save Entry & Generate SMS")

# -----------------------------------------------------------------
# 💾 SAVE DATA TO EXCEL & LOG SMS
# -----------------------------------------------------------------
if submitted:
    # Validation: Ensure important fields are not left empty
    if not (project and b_code and capacity and rating and assigned_team):
        st.error("❌ Error! Please fill all the fields before saving.")
    else:
        # Create a dictionary of the entered data
        input_data = {
            "Date": [comp_date.strftime("%Y-%m-%d")],
            "Project Name": [project],
            "Branch Code": [b_code],
            "Branch Name": [b_name],
            "Generator Capacity": [capacity],
            "Rating": [rating],
            "Assigned Team Member": [assigned_team],
            "Remarks": [remarks]
        }
        
        # Convert to Pandas DataFrame
        df_new = pd.DataFrame(input_data)
        excel_file = "complaints.xlsx"
        
        # If Excel file already exists, append data; otherwise create new file
        if os.path.exists(excel_file):
            df_old = pd.read_excel(excel_file)
            df_final = pd.concat([df_old, df_new], ignore_index=True)
        else:
            df_final = df_new
            
        # Save to Excel file
        df_final.to_excel(excel_file, index=False)
        
        # Display Success Message
        st.success("🎉 Success! Data has been successfully saved to the Excel database.")
        
        # Show Generated SMS on Screen
        st.markdown("### 📱 Dispatched SMS Preview")
        st.info(f"""
        **To:** {assigned_team}  
        **Message:** Nayi complaint assign hui hai.  
        * **Branch:** {b_name} ({b_code})  
        * **Capacity/Rating:** {capacity} / {rating}  
        * **Remarks:** {remarks if remarks else 'None'}
        """)
import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Page Settings
st.set_page_config(page_title="Data Entry Hub", page_icon="📝", layout="wide")

# App Main Title
st.title("📋 Detailed Complaint & Asset Entry Portal")
st.write("Meharbani karke generator aur complaint ki mukammal details is form mein darj karein.")

# 1. BACKUP PROFORMA (Branch Code to Name Mapping)
branch_proforma = {
    "BR-001": "Lahore Main Office (Gulberg)",
    "BR-002": "Karachi Saddar Head Office",
    "BR-003": "Islamabad Blue Area Branch",
    "BR-004": "Faisalabad Clock Tower Complex",
    "BR-005": "Multan Cantt Regional Office"
}

projects = ["Project Alpha", "Project Beta", "Project Delta", "Project Titan"]
team_members = ["Ali Khan", "Zainab Ahmed", "Bilal Siddiqui", "Hamza Usman"]

# -----------------------------------------------------------------
# 🧱 DETAILED DATA ENTRY FORM
# -----------------------------------------------------------------
with st.form("detailed_entry_form", clear_on_submit=True):
    
    st.markdown("### 🔴 Section 1: Ticket & Location Info")
    col1, col2 = st.columns(2)
    
    with col1:
        # Date Input (Calendar Widget)
        comp_date = st.date_input("Select Date / Tareekh:", datetime.today())
        
        # Project Selection Dropdown
        project = st.selectbox("Select Project Name:", [""] + projects)
        
    with col2:
        # Branch Code Dropdown
        b_code = st.selectbox("Select Branch Code:", [""] + list(branch_proforma.keys()))
        
        # Automatic Branch Name Mapping (Read-Only Field)
        b_name = branch_proforma.get(b_code, "")
        st.text_input("Branch Name (Automated via Proforma):", value=b_name, disabled=True)
        
    st.markdown("---")
    st.markdown("### ⚡ Section 2: Generator Specifications")
    col3, col4 = st.columns(2)
    
    with col3:
        # Generator Capacity Field
        capacity = st.text_input("Generator Capacity (e.g., 50 KVA, 100 KVA):", placeholder="Enter capacity here...")
        
    with col4:
        # Generator Rating Field
        rating = st.text_input("Generator Rating (e.g., Prime, Standby, Continuous):", placeholder="Enter rating here...")
        
    st.markdown("---")
    st.markdown("### 🛠️ Section 3: Assignment & Action Details")
    
    # Team Member Assignment
    assigned_team = st.selectbox("Assign Complaint To (Team Member):", [""] + team_members)
    
    # Remarks Text Area
    remarks = st.text_area("Remarks / Issue Description / Special Instructions:", placeholder="Type complaint or technical details here...")
    
    # Form Submission Button
    submitted = st.form_submit_button("💾 Save Entry & Dispatch SMS")

# -----------------------------------------------------------------
# 📊 BACKEND ACTION AFTER SUBMISSION
# -----------------------------------------------------------------
if submitted:
    # Checking if mandatory fields are empty
    if not (project and b_code and capacity and rating and assigned_team):
        st.error("❌ Form Incomplete! Meharbani karke tamam details lazmi darj karein.")
    else:
        # Preparing Data Structure for Excel Sheet
        entry_details = {
            "Date": [comp_date.strftime("%Y-%m-%d")],
            "Project Name": [project],
            "Branch Code": [b_code],
            "Branch Name": [b_name],
            "Generator Capacity": [capacity],
            "Rating": [rating],
            "Assigned Team Member": [assigned_team],
            "Remarks / Description": [remarks]
        }
        
        df_new = pd.DataFrame(entry_details)
        excel_file = "complaints.xlsx"
        
        # Excel Append Logic
        if os.path.exists(excel_file):
            df_old = pd.read_excel(excel_file)
            df_final = pd.concat([df_old, df_new], ignore_index=True)
        else:
            df_final = df_new
            
        df_final.to_excel(excel_file, index=False)
        
        # Success Banner
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
