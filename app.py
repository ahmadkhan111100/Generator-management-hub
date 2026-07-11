import streamlit as st
from PIL import Image
import os

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
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --------------------------------------------------
# Header
# --------------------------------------------------

col1, col2, col3 = st.columns([2,6,2])

with col1:
    if os.path.exists("images/logo.png"):
        st.image("images/logo.png", width=180)

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

st.markdown("---")

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
# Hero Banner
# --------------------------------------------------

if os.path.exists("images/hero.jpg"):
    st.image("images/hero.jpg", use_container_width=True)

st.markdown("""
<div class="hero-title">
<h1>Operation & Maintenance Solutions</h1>
<h3>Electrical • Mechanical • Solar • Engine Overhauling • Agriculture • Chemicals</h3>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# --------------------------------------------------
# About Company
# --------------------------------------------------

st.markdown("## About F&A Enterprises")

left, right = st.columns([3,2])

with left:

    st.write("""

F&A Enterprises provides complete Engineering,
Operation & Maintenance solutions across Pakistan.

Our company specializes in:

- Electrical Engineering
- Mechanical Engineering
- Engine Overhauling
- Generator Maintenance
- Solar Panel Supply
- Solar Installation
- Industrial Chemicals
- Agriculture Products
- Computer Accessories
- Electronic Accessories

We believe in quality workmanship, timely delivery,
professional staff and customer satisfaction.

""")

with right:

    if os.path.exists("images/about.jpg"):
        st.image("images/about.jpg", use_container_width=True)

st.divider()

# --------------------------------------------------
# Services
# --------------------------------------------------

st.markdown("# Our Services")

col1,col2,col3 = st.columns(3)

with col1:

    st.markdown("### ⚡ Electrical")

    st.success("""
Installation

Maintenance

Troubleshooting

Power Distribution

HT/LT Panels

Transformer Works
""")

with col2:

    st.markdown("### ⚙ Mechanical")

    st.info("""
Engine Overhauling

Pump Maintenance

Compressors

Industrial Machinery

Fabrication

Maintenance Contracts
""")

with col3:

    st.markdown("### ☀ Solar")

    st.warning("""
Solar Panels

Hybrid Systems

Installation

Maintenance

Battery Backup

On Grid Solutions
""")

st.divider()

# --------------------------------------------------
# Product Categories
# --------------------------------------------------

st.markdown("# Products")

products = [
    ("Power Systems","images/power.jpg"),
    ("Industrial Machinery","images/machinery.jpg"),
    ("Alternative Energy","images/solar.jpg"),
    ("CAT Genuine Parts","images/parts.jpg"),
    ("Engine Overhauling","images/engines.jpg"),
    ("Construction Equipment","images/construction.jpg")
]

for i in range(0,len(products),3):

    cols = st.columns(3)

    for col,(title,image) in zip(cols,products[i:i+3]):

        with col:

            if os.path.exists(image):
                st.image(image,use_container_width=True)

            st.markdown(
                f"""
                <div class="product-card">
                <h3>{title}</h3>
                </div>
                """,
                unsafe_allow_html=True
            )

st.divider()

# --------------------------------------------------
# Statistics
# --------------------------------------------------

st.markdown("# Company Statistics")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("Projects","500+")

with c2:
    st.metric("Clients","150+")

with c3:
    st.metric("Engineers","40+")

with c4:
    st.metric("Branches","Nationwide")

st.divider()

# --------------------------------------------------
# Contact
# --------------------------------------------------

st.markdown("# Contact Us")

name = st.text_input("Full Name")

email = st.text_input("Email Address")

phone = st.text_input("Phone Number")

subject = st.text_input("Subject")

message = st.text_area("Message")

if st.button("Send Inquiry"):

    if name == "" or email == "" or message == "":
        st.error("Please fill all required fields.")
    else:
        st.success("Your inquiry has been submitted successfully.")

st.divider()

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("""

<center>

<h3>F&A Enterprises</h3>

Operation & Maintenance | Electrical | Mechanical | Solar Solutions

📞 +92-300-0000000

✉ info@faenterprises.com

© 2026 All Rights Reserved

</center>

""",unsafe_allow_html=True)

html, body, [class*="css"] {
    font-family: "Segoe UI", Arial, sans-serif;
}

/* Main background */
.stApp{
    background:#f5f5f5;
}

/* Remove Streamlit header/footer */
header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* -------------------------
   Company Header
------------------------- */

.toptext{
    padding-top:15px;
    text-align:center;
}.toptext h1{
    color:#111;
    font-size:42px;
    font-weight:800;
    margin-bottom:5px;
}

.toptext h3{
    color:#ffb400;
    font-size:22px;
    font-weight:700;
}

/* -------------------------
   Navigation Bar
------------------------- */

.menu{
    display:flex;
    justify-content:center;
    align-items:center;
    flex-wrap:wrap;
    gap:35px;
    background:#ffb400;
    padding:15px;
    border-radius:8px;
    margin-bottom:25px;
}

.menu a{
    color:#000;
    text-decoration:none;
    font-size:17px;
    font-weight:700;
    transition:.3s;
}

.menu a:hover{
    color:white;
}

/* -------------------------
   Hero
------------------------- */

.hero-title{
    text-align:center;
    margin-top:20px;
    margin-bottom:40px;
}

.hero-title h1{
    font-size:46px;
    color:#111;
    font-weight:800;
}

.hero-title h3{
    color:#666;
    font-size:22px;
}

/* -------------------------
   Section Titles
------------------------- */

h2{
    color:#111;
    font-weight:800;
    margin-top:20px;
}

h3{
    color:#222;
}

/* -------------------------
   Product Cards
------------------------- */

.product-card{

    background:white;

    padding:18px;

    border-radius:10px;

    text-align:center;

    margin-top:-5px;

    margin-bottom:20px;

    box-shadow:0px 5px 18px rgba(0,0,0,.15);

    transition:.35s;
}

.product-card:hover{

    transform:translateY(-8px);

    box-shadow:0px 15px 35px rgba(0,0,0,.30);
}

.product-card h3{

    margin:0;

    color:#111;

    font-size:24px;
}

/* -------------------------
   Streamlit Images
------------------------- */

img{

    border-radius:8px;
}

/* -------------------------
   Buttons
------------------------- */

.stButton>button{

    background:#ffb400;

    color:black;

    border:none;

    border-radius:8px;

    font-weight:700;

    width:100%;

    height:48px;

    transition:.3s;
}

.stButton>button:hover{

    background:black;

    color:white;
}

/* -------------------------
   Text Inputs
------------------------- */

.stTextInput input{

    border-radius:6px;

    border:1px solid #cccccc;
}

.stTextArea textarea{

    border-radius:6px;

    border:1px solid #cccccc;
}

/* -------------------------
   Metrics
------------------------- */

[data-testid="stMetric"]{

    background:white;

    padding:15px;

    border-radius:10px;

    text-align:center;

    box-shadow:0px 4px 12px rgba(0,0,0,.12);
}

/* -------------------------
   Success / Info / Warning
------------------------- */

.stAlert{

    border-radius:10px;
}

/* -------------------------
   Footer
------------------------- */

footer{

    visibility:hidden;
}

.footer{

    background:#111;

    color:white;

    padding:30px;

    text-align:center;

    border-radius:10px;

    margin-top:50px;
}

/* -------------------------
   Divider
------------------------- */

hr{

    border:1px solid #dddddd;
}

/* -------------------------
   Responsive
------------------------- */

@media(max-width:992px){

.hero-title h1{

    font-size:34px;
}

.hero-title h3{

    font-size:18px;
}

.toptext h1{

    font-size:30px;
}

.menu{

    gap:15px;
}

}

@media(max-width:600px){

.menu{

    flex-direction:column;
}

.hero-title h1{

    font-size:28px;
}

.hero-title h3{

    font-size:16px;
}

.toptext h1{

    font-size:24px;
}

.product-card h3{

    font-size:20px;
}

}
import time

slider_images = [
    "images/slider1.jpg",
    "images/slider2.jpg",
    "images/slider3.jpg",
    "images/slider4.jpg"
]

slider = st.empty()

for image in slider_images:
    slider.image(image, use_container_width=True)
    time.sleep(2)
    st.markdown("## Company Statistics")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Completed Projects","650+")
col2.metric("Happy Clients","220+")
col3.metric("Engineers","48")
col4.metric("Branches","Pakistan")
st.markdown("## Company Statistics")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Completed Projects","650+")
col2.metric("Happy Clients","220+")
col3.metric("Engineers","48")
col4.metric("Branches","Pakistan")
st.markdown("## What Our Clients Say")

c1,c2,c3 = st.columns(3)

with c1:
    st.info("""
⭐⭐⭐⭐⭐

Excellent maintenance services.

**National Bank**
""")

with c2:
    st.success("""
⭐⭐⭐⭐⭐

Professional Solar Installation.

**Meezan Bank**
""")

with c3:
    st.warning("""
⭐⭐⭐⭐⭐

Highly Recommended.

**HBL**
""")
    st.markdown("## Our Clients")

c1,c2,c3,c4,c5 = st.columns(5)

with c1:
    st.image("images/client1.png")

with c2:
    st.image("images/client2.png")

with c3:
    st.image("images/client3.png")

with c4:
    st.image("images/client4.png")

with c5:
    st.image("images/client5.png")
    st.markdown("## Office Location")

st.components.v1.iframe(
    "https://maps.google.com/maps?q=Lahore&t=&z=13&ie=UTF8&iwloc=&output=embed",
    height=450
)
documents/
Company_Profile.pdf
with open("documents/Company_Profile.pdf","rb") as pdf:

    st.download_button(
        label="📄 Download Company Profile",
        data=pdf,
        file_name="F&A_Company_Profile.pdf",
        mime="application/pdf"
    )
    st.markdown("""
<a href="https://wa.me/923001234567" target="_blank">
<div style="
position:fixed;
bottom:25px;
right:25px;
background:#25D366;
padding:18px;
border-radius:50%;
font-size:28px;
color:white;
z-index:9999;
">
💬
</div>
</a>
""", unsafe_allow_html=True)
    requirements.txt
    streamlit
Pillow
pandas
numpy
openpyxl
generator-management-hub/
│
├── app.py
├── style.css
├── requirements.txt
│
├── documents/
│      Company_Profile.pdf
│
└── images/
       logo.png
       hero.jpg
       about.jpg

       slider1.jpg
       slider2.jpg
       slider3.jpg
       slider4.jpg

       power.jpg
       machinery.jpg
       solar.jpg
       parts.jpg
       engines.jpg
       construction.jpg

       client1.png
       client2.png
       client3.png
       client4.png
       client5.png
    generator-management-hub/
│
├── app.py                  # Home
├── style.css
├── requirements.txt
│
├── pages/
│   ├── 1_About.py
│   ├── 2_Services.py
│   ├── 3_Products.py
│   ├── 4_Projects.py
│   ├── 5_Careers.py
│   ├── 6_Contact.py
│   └── 7_Admin.py
│
├── images/
└── documents/
