import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import openpyxl
import os

class ComplaintSoftware:
    def __init__(self, root):
        self.root = root
        self.root.title("Complaint Management & Dispatch System")
        self.root.geometry("600x650")
        self.root.configure(bg="#f4f6f9")

        # 1. Backup Proforma (Branch Code to Branch Name Mapping)
        self.branch_proforma = {
            "BR-001": "Lahore Main Office",
            "BR-002": "Karachi Saddar Branch",
            "BR-003": "Islamabad Blue Area",
            "BR-004": "Faisalabad Clock Tower",
            "BR-005": "Multan Cantt Branch"
        }

        # Project Names & Team Members Lists
        self.projects = ["Project Alpha", "Project Beta", "Project Delta", "Project Titan"]
        self.team_members = ["Ali Khan", "Zainab Ahmed", "Bilal Siddiqui", "Hamza Usman"]

        # Main Heading
        heading = tk.Label(root, text="Complaint Registration Form", font=("Arial", 16, "bold"), bg="#f4f6f9", fg="#333")
        heading.pack(pady=15)

        # Form Container Frame
        form_frame = tk.Frame(root, bg="white", bd=1, relief="solid", padx=20, pady=20)
        form_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # ---- FIELDS ----

        # Date Field (Calendar)
        tk.Label(form_frame, text="Select Date:", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", pady=8)
        self.date_entry = DateEntry(form_frame, width=25, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=0, column=1, pady=8, sticky="w")

        # Project Name Dropdown
        tk.Label(form_frame, text="Project Name:", font=("Arial", 10, "bold"), bg="white").grid(row=1, column=0, sticky="w", pady=8)
        self.project_var = tk.StringVar()
        self.project_cb = ttk.Combobox(form_frame, textvariable=self.project_var, values=self.projects, width=25, state="readonly")
        self.project_cb.grid(row=1, column=1, pady=8, sticky="w")

        # Branch Code Dropdown
        tk.Label(form_frame, text="Branch Code:", font=("Arial", 10, "bold"), bg="white").grid(row=2, column=0, sticky="w", pady=8)
        self.branch_code_var = tk.StringVar()
        self.branch_code_cb = ttk.Combobox(form_frame, textvariable=self.branch_code_var, values=list(self.branch_proforma.keys()), width=25, state="readonly")
        self.branch_code_cb.grid(row=2, column=1, pady=8, sticky="w")
        self.branch_code_cb.bind("<<ComboboxSelected>>", self.update_branch_name)

        # Automated Branch Name (Read-Only)
        tk.Label(form_frame, text="Branch Name:", font=("Arial", 10, "bold"), bg="white").grid(row=3, column=0, sticky="w", pady=8)
        self.branch_name_var = tk.StringVar()
        self.branch_name_entry = tk.Entry(form_frame, textvariable=self.branch_name_var, width=28, state="readonly", readonlybackground="#e9ecef")
        self.branch_name_entry.grid(row=3, column=1, pady=8, sticky="w")

        # Generator Capacity
        tk.Label(form_frame, text="Generator Capacity:", font=("Arial", 10, "bold"), bg="white").grid(row=4, column=0, sticky="w", pady=8)
        self.capacity_entry = tk.Entry(form_frame, width=28)
        self.capacity_entry.grid(row=4, column=1, pady=8, sticky="w")

        # Generator Rating
        tk.Label(form_frame, text="Generator Rating:", font=("Arial", 10, "bold"), bg="white").grid(row=5, column=0, sticky="w", pady=8)
        self.rating_entry = tk.Entry(form_frame, width=28)
        self.rating_entry.grid(row=5, column=1, pady=8, sticky="w")

        # Assign Team Member Dropdown
        tk.Label(form_frame, text="Assign Team Member:", font=("Arial", 10, "bold"), bg="white").grid(row=6, column=0, sticky="w", pady=8)
        self.team_var = tk.StringVar()
        self.team_cb = ttk.Combobox(form_frame, textvariable=self.team_var, values=self.team_members, width=25, state="readonly")
        self.team_cb.grid(row=6, column=1, pady=8, sticky="w")

        # Remarks Text Area
        tk.Label(form_frame, text="Remarks:", font=("Arial", 10, "bold"), bg="white").grid(row=7, column=0, sticky="nw", pady=8)
        self.remarks_text = tk.Text(form_frame, width=30, height=4, bd=1, relief="solid")
        self.remarks_text.grid(row=7, column=1, pady=8, sticky="w")

        # Submit Button
        submit_btn = tk.Button(root, text="Submit & Send SMS Alert", font=("Arial", 11, "bold"), bg="#28a745", fg="white", bd=0, padx=20, pady=10, command=self.submit_complaint)
        submit_btn.pack(pady=15)

    # Function to automatically update branch name based on branch code
    def update_branch_name(self, event):
        selected_code = self.branch_code_var.get()
        branch_name = self.branch_proforma.get(selected_code, "")
        self.branch_name_var.set(branch_name)

    # Function to save data and simulate SMS
    def submit_complaint(self):
        # Gathering Data
        comp_date = self.date_entry.get()
        project = self.project_var.get()
        b_code = self.branch_code_var.get()
        b_name = self.branch_name_var.get()
        capacity = self.capacity_entry.get().strip()
        rating = self.rating_entry.get().strip()
        assigned_team = self.team_var.get()
        remarks = self.remarks_text.get("1.0", tk.END).strip()

        # Validation
        if not (project and b_code and capacity and rating and assigned_team):
            messagebox.showerror("Error", "Meharbani karke tamam zaroori fields fill karein!")
            return

        # 2. Save Data to Excel File
        excel_file = "complaints.xlsx"
        row_data = [comp_date, project, b_code, b_name, capacity, rating, assigned_team, remarks]

        if not os.path.exists(excel_file):
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "Complaints"
            ws.append(["Date", "Project Name", "Branch Code", "Branch Name", "Generator Capacity", "Rating", "Assigned To", "Remarks"])
        else:
            wb = openpyxl.load_workbook(excel_file)
            ws = wb.active

        ws.append(row_data)
        wb.save(excel_file)

        # 3. Mock SMS Generation (Console Log)
        self.generate_sms_log(assigned_team, b_name, capacity, rating)

        # Success Message
        messagebox.showinfo("Success", f"Complaint register ho gayi hai aur data Excel mein save ho chuka hai.\nSMS alert generated for {assigned_team}!")

        # Reset Form Fields
        self.clear_form()

    def generate_sms_log(self, team_member, branch, capacity, rating):
        sms_text = (
            f"\n--- 📱 GENERATED SMS ALERT ---\n"
            f"To: {team_member}\n"
            f"Message: Nayi complaint assign hui hai. Branch: {branch}. "
            f"Generator Capacity: {capacity}, Rating: {rating}. Kindly check and resolve as soon as possible.\n"
            f"-------------------------------\n"
        )
        print(sms_text)

    def clear_form(self):
        self.project_cb.set('')
        self.branch_code_cb.set('')
        self.branch_name_var.set('')
        self.capacity_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)
        self.team_cb.set('')
        self.remarks_text.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ComplaintSoftware(root)
    root.mainloop()
