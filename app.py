import streamlit as st

st.set_page_config(layout="wide")

st.title("PRODUCTS")
import streamlit as st
from PIL import Image
import base64

st.set_page_config(
    page_title="F&A Enterprises",
    page_icon="⚡",
    layout="wide"
)

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# --------------------------
# Header
# --------------------------

col1,col2,col3=st.columns([2,6,2])

with col1:
    st.image("images/logo.png", width=200)

with col2:
    st.markdown(
    """
    <div class='toptext'>
    <h2>LET'S DO THE WORK.</h2>
    </div>
    """,
    unsafe_allow_html=True
    )

with col3:
    st.write("📞 +92-300-0000000")
    st.write("✉ info@faenterprises.com")


st.markdown("---")

# Navigation

menu="""
<div class="menu">
<a href="#">HOME</a>
<a href="#">COMPANY</a>
<a href="#">PRODUCTS</a>
<a href="#">SERVICES</a>
<a href="#">PROJECTS</a>
<a href="#">CONTACT</a>
</div>
"""

st.markdown(menu, unsafe_allow_html=True)

# -----------------------
# Hero Image
# -----------------------

st.image("images/hero.jpg", use_container_width=True)

st.markdown(
"""
<div class='hero'>
<h1>Operation & Maintenance Services</h1>

<h3>Electrical | Mechanical | Engine Overhauling | Solar | Agriculture | Chemicals</h3>

</div>
""",
unsafe_allow_html=True
)

st.markdown("<br>",unsafe_allow_html=True)

# -------------------------
# About
# -------------------------

st.header("About F&A Enterprises")

st.write("""

F&A Enterprises provides professional Operation &
Maintenance solutions across Pakistan.

✔ Electrical Works

✔ Mechanical Works

✔ Engine Overhauling

✔ Solar Panel Supply

✔ Solar Installation

✔ Computer Accessories

✔ Electronic Accessories

✔ Industrial Chemicals

✔ Agriculture Products

""")

# ----------------------------
# Services
# ----------------------------

st.header("Our Services")

col1,col2,col3=st.columns(3)

with col1:

    st.info("""
⚡ Electrical Services

• Installation

• Maintenance

• Troubleshooting

• Power Systems

""")

with col2:

    st.success("""
⚙ Mechanical Services

• Pumps

• Motors

• Compressors

• Engine Overhauling

""")

with col3:

    st.warning("""
☀ Solar Solutions

• Solar Panels

• Installation

• Maintenance

• Hybrid Systems

""")

# --------------------------

st.header("Products")

col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric("Electrical","150+")

with col2:
    st.metric("Mechanical","95+")

with col3:
    st.metric("Solar","80+")

with col4:
    st.metric("Agriculture","120+")


st.markdown("---")

st.header("Contact")

name=st.text_input("Name")

email=st.text_input("Email")

message=st.text_area("Message")

if st.button("Send Inquiry"):
    st.success("Thank you! We will contact you soon.")


st.markdown(
"""
<hr>

<center>

© 2026 F&A Enterprises

</center>

""",
unsafe_allow_html=True
)body{
background:#ffffff;
}

.toptext{
text-align:center;
font-weight:bold;
color:#111;
}

.menu{
display:flex;
justify-content:center;
gap:40px;
padding:15px;
background:#FFC300;
font-weight:bold;
}

.menu a{
text-decoration:none;
color:black;
font-size:18px;
}

.menu a:hover{
color:#444;
}

.hero{
position:absolute;
top:270px;
left:0;
right:0;
text-align:center;
color:white;
font-weight:bold;
text-shadow:2px 2px 10px black;
}

.hero h1{
font-size:60px;
}

.hero h3{
font-size:25px;
}

h1,h2,h3{
font-family:Arial;
}

.stButton button{
background:#FFC300;
color:black;
font-weight:bold;
border-radius:8px;
}

.stButton button:hover{
background:#111;
color:white;
}pip install streamlit pillow
streamlit run app.py
project/
│
├── app.py
├── images/
│     power.jpg
│     machinery.jpg
│     solar.jpg
│     parts.jpg
│     engines.jpg
│     construction.jpg
    import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
"""
<h1 style='text-align:center;'>PRODUCTS</h1>
<hr style='width:80px;border:2px solid #f4b400;margin:auto;'>
""",
unsafe_allow_html=True
)

products = [
    ("Power Systems", "images/power.jpg"),
    ("Machinery", "images/machinery.jpg"),
    ("Alternative Energy Solutions", "images/solar.jpg"),
    ("CAT Genuine Parts", "images/parts.jpg"),
    ("Engine Overhauling", "images/engines.jpg"),
    ("Construction Equipment", "images/construction.jpg"),
]

for i in range(0, len(products), 3):

    cols = st.columns(3)

    for col, (title, img) in zip(cols, products[i:i+3]):

        with col:

            st.image(img, use_container_width=True)

            st.markdown(
                f"""
                <div style="
                    background:white;
                    text-align:center;
                    padding:20px;
                    margin-top:-5px;
                    font-size:30px;
                    font-weight:500;
                    box-shadow:0px 3px 12px rgba(0,0,0,0.15);
                    border-radius:0px 0px 8px 8px;">
                    {title}
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<br>", unsafe_allow_html=True)
    .product-card{
    transition:0.4s;
}

.product-card:hover{
    transform:translateY(-8px);
    box-shadow:0 15px 30px rgba(0,0,0,.3);
}
---------------------------------------------
               PRODUCTS
---------------------------------------------

+----------------+----------------+----------------+
|     Image      |     Image      |     Image      |
+----------------+----------------+----------------+
| Power Systems  | Machinery      | Solar Energy   |
+----------------+----------------+----------------+

+----------------+----------------+----------------+
|     Image      |     Image      |     Image      |
+----------------+----------------+----------------+
| Genuine Parts  | Engine Repair  | Construction   |
+----------------+----------------+----------------+
