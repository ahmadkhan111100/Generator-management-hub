import os
import time
import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="F&A Enterprises",
    page_icon="⚡",
    layout="wide"
)

# --------------------------------------------------
# Load CSS
# --------------------------------------------------

if os.path.exists("style.css"):
    with open("style.css", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --------------------------------------------------
# Header
# --------------------------------------------------

col1, col2, col3 = st.columns([2, 6, 2])

with col1:
    if os.path.exists("images/logo.png"):
        st.image("images/logo.png", width=170)

with col2:
    st.markdown("""
    <div class="toptext">
        <h1>F&A ENTERPRISES</h1>
        <h3>LET'S DO THE WORK.</h3>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.write("📞 +92-300-0000000")
    st.write("✉ info@faenterprises.com")

st.divider()

# --------------------------------------------------
# Navigation
# --------------------------------------------------

st.markdown("""
<div class="menu">
<a href="#">HOME</a>
<a href="#">ABOUT</a>
<a href="#">SERVICES</a>
<a href="#">PRODUCTS</a>
<a href="#">PROJECTS</a>
<a href="#">CONTACT</a>
</div>
""", unsafe_allow_html=True)

st.write("")

# --------------------------------------------------
# Hero Slider
# --------------------------------------------------

slider_images = [
    "images/slider1.jpg",
    "images/slider2.jpg",
    "images/slider3.jpg",
    "images/slider4.jpg"
]

placeholder = st.empty()

for img in slider_images:
    if os.path.exists(img):
        placeholder.image(img, use_container_width=True)
        time.sleep(1)

st.markdown("""
<div class="hero-title">
<h1>Operation & Maintenance Solutions</h1>
<h3>Electrical • Mechanical • Solar • Generator • Agriculture • Chemicals</h3>
</div>
""", unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# About
# --------------------------------------------------

st.header("About F&A Enterprises")

left, right = st.columns([3, 2])

with left:
    st.markdown("""
F&A Enterprises provides complete Engineering,
Operation & Maintenance services throughout Pakistan.

### Our Expertise

- Electrical Engineering
- Mechanical Engineering
- Engine Overhauling
- Generator Maintenance
- Solar Energy Solutions
- Industrial Chemicals
- Agriculture Products
- Computer Accessories
- Electronic Equipment

We are committed to quality, safety and customer satisfaction.
""")

with right:
    if os.path.exists("images/about.jpg"):
        st.image("images/about.jpg", use_container_width=True)

st.divider()

# --------------------------------------------------
# Services
# --------------------------------------------------

st.header("Our Services")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("""
### Electrical

- Installation
- Maintenance
- Troubleshooting
- HT/LT Panels
- Transformers
""")

with c2:
    st.info("""
### Mechanical

- Engine Overhauling
- Pumps
- Compressors
- Fabrication
- AMC Services
""")

with c3:
    st.warning("""
### Solar

- Solar Panels
- Hybrid Systems
- On Grid
- Battery Backup
- Installation
""")

st.divider()

# --------------------------------------------------
# Products
# --------------------------------------------------

st.header("Products")

products = [
    ("Power Systems", "images/power.jpg"),
    ("Industrial Machinery", "images/machinery.jpg"),
    ("Solar Systems", "images/solar.jpg"),
    ("CAT Genuine Parts", "images/parts.jpg"),
    ("Engines", "images/engines.jpg"),
    ("Construction Equipment", "images/construction.jpg"),
]

for i in range(0, len(products), 3):

    cols = st.columns(3)

    for col, (title, img) in zip(cols, products[i:i+3]):

        with col:

            if os.path.exists(img):
                st.image(img, use_container_width=True)

            st.markdown(f"### {title}")

st.divider()

# --------------------------------------------------
# Statistics
# --------------------------------------------------

st.header("Company Statistics")

m1, m2, m3, m4 = st.columns(4)

m1.metric("Projects", "650+")
m2.metric("Clients", "220+")
m3.metric("Engineers", "48")
m4.metric("Branches", "Pakistan")

st.divider()

# --------------------------------------------------
# Testimonials
# --------------------------------------------------

st.header("What Our Clients Say")

t1, t2, t3 = st.columns(3)

with t1:
    st.info("⭐⭐⭐⭐⭐\n\nExcellent maintenance services.\n\n**National Bank**")

with t2:
    st.success("⭐⭐⭐⭐⭐\n\nProfessional Solar Installation.\n\n**Meezan Bank**")

with t3:
    st.warning("⭐⭐⭐⭐⭐\n\nHighly Recommended.\n\n**HBL**")

st.divider()

# --------------------------------------------------
# Clients
# --------------------------------------------------

st.header("Our Clients")

cols = st.columns(5)

for i in range(5):
    logo = f"images/client{i+1}.png"
    if os.path.exists(logo):
        cols[i].image(logo)

st.divider()

# --------------------------------------------------
# Company Profile
# --------------------------------------------------

if os.path.exists("documents/Company_Profile.pdf"):

    with open("documents/Company_Profile.pdf", "rb") as pdf:

        st.download_button(
            "📄 Download Company Profile",
            pdf,
            file_name="F&A_Company_Profile.pdf",
            mime="application/pdf"
        )

st.divider()

# --------------------------------------------------
# Contact Form
# --------------------------------------------------

st.header("Contact Us")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
subject = st.text_input("Subject")
message = st.text_area("Message")

if st.button("Send Inquiry"):

    if not name or not email or not message:
        st.error("Please fill all required fields.")
    else:
        st.success("Inquiry submitted successfully.")

st.divider()

# --------------------------------------------------
# Google Map
# --------------------------------------------------

st.header("Office Location")

st.components.v1.iframe(
    "https://maps.google.com/maps?q=Lahore&t=&z=13&ie=UTF8&iwloc=&output=embed",
    height=450
)

st.divider()

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("""
<div style="text-align:center;padding:20px">
<h3>F&A Enterprises</h3>
<p>Electrical | Mechanical | Solar | Generator Solutions</p>
<p>📞 +92-300-0000000</p>
<p>✉ info@faenterprises.com</p>
<p>© 2026 All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)
