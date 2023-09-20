import streamlit as st
from PIL import Image
from pathlib import Path


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
# resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "cv_img.png"


PAGE_TITLE = "CV"
PAGE_ICON = ":computer:"


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout='wide')


with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


@st.cache_data(show_spinner=False)
def read_image():
    return Image.open(profile_pic)

col_ph, col_name = st.columns([1, 3], gap="large")
col_ph.write("\n\n\n")
col_ph.image(read_image(), use_column_width=True)

col_name.header("Kseniya Shymborskaya")
col_name.write("\n")

col_name.subheader("Data Scientist | AI Engineer")
col_name.write("\n")

col_name.write(":email: k.shymborskaya@gmail.com")
col_name.write(":telephone_receiver: +5491154931032")

col_name.markdown(
    """
        <a href='https://wa.me/5491154931032'><img src='https://img.shields.io/badge/WhatsApp-25D366?style=flat&logo=whatsapp&logoColor=white' alt='WhatsApp' height='25'>
        <a href='https://t.me/deadchicsocool'><img src='https://img.shields.io/badge/Telegram-2CA5E0?style=flat&logo=telegram&logoColor=white' alt='Telegram' height='25'></a>
        <a href='https://www.linkedin.com/in/kseniya-shymborskaya-4058b61b0/'><img src='https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=flat&logo=linkedin&logoColor=white' alt='LinkedIn' height='25'></a>
        <a href='https://github.com/svspirivm'><img src='https://img.shields.io/badge/GitHub-%23121011.svg?style=flat&logo=github&logoColor=white' alt='GitHub' height='25'></a>
    """, 
    unsafe_allow_html=True
)
col_name.write("\n")

st.divider()

left, right = st.columns([1, 2.5], gap="large")

with left.expander("Programming Languages", expanded=True):
    st.write(
        """
        - Python
        - C++
        - R
        """
    )
    st.write("\n")

with left.expander("Cloud Technologies", expanded=True):
    st.write("""
            - Google Cloud Platform
            - Microsoft Azure
            """)
    st.write("\n")

with left.expander("Hard Skills", expanded=True):
    st.write(
        """
        - Deep Learning (torch)
        - Image Processing (OpenCV)
        - Machine Learning 
        - Data Analysis
        - Predictive Modeling
        - Data Visualization
        - NLP
        - SQL
        """
    )
    st.write("\n")

with left.expander("Languages"):
    st.write(
        """
        - English  —  fluent
        - Belarusian  —  native
        - Russian  —  native
        - Turkish  —  intermediate
        - Spanish  —  beginner
        """
    )
    st.write("\n")

with left.expander("Education"):
    st.caption("2019  — 2022, Belarusian State University")
    st.write("""
            Applied Mathematics and 
            Computer Science
            """)
    st.write("\n")

    
right.subheader(":pushpin: AI Engineer  —  Nadon Media")
right.write("06/2023  —  09/2023")
right.write(":construction: **Intelligent Multimodal Video Editor**")
_, col_proj = right.columns([1, 15])
with col_proj:
    st.write(
        """
        - Solely designed and implemented end-to-end cloud-based 
        solution with a web interface;
        - Orchestrated the operation of multiple language and computer 
        vision models within the processing pipeline to achieve seamless 
        multimodal analysis for autonomous video editing;
        - Integrated external service access capabilities, enabling the 
        leveraging of insights from multimodal analysis for the 
        retrieval of relevant data for enhancing dynamic content in video editing;
        - Deployed the product to Microsoft Azure Platform and configured the cloud
        environment for batch video processing.
        """
    )

right.subheader(":pushpin: Data Scientist  —  EPAM Systems")
right.write("04/2021  —  01/2023")

right.write(":construction: **Computer Vision for Inventory Management**")
_, col_proj = right.columns([1, 15])
with col_proj:
    col_proj.write(
        """
        - Developed algorithms for product detection and recognition 
        in densely packed setups;
        - Designed deep learning models 
            for stock keeping units placement optimization;
        - Employed metric learning techniques to create an embedded model for 
        large-scale object detection and search;
        - Built Google Cloud Platform pipelines to orchestrate ML workflows.
        """
    )


right.write(":construction: **AR Makeup Try-On**")
_, col_proj = right.columns([1, 15])
with col_proj:
    col_proj.write(
        """
        - Developed a real-time instance segmentation model optimized for mobile devices;
        - Curated collection and integration of custom data to enhance model robustness;
        - Established pipelines for computer vision model training and evaluation;
        - Designed evaluation protocols to assess model performance 
        and identify improvement opportunities.
        """
    )

right.write(":construction: **AI-powered Skin Analysis**")
_, col_proj = right.columns([1, 15])
with col_proj:
    col_proj.write(
        """
        - Conducted extensive research in the domain field, leveraging insights 
        from pertinent literature to address project-specific challenges;
        - Devised experiments and data augmentation techniques to maximize limited data utilization;
        - Presented updates to the customer, using their 
        domain expertise to refine implementation process;
        - Collaborated with cross-functional teams to streamline the product development.
        """
    )
