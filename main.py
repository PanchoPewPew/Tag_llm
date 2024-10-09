import streamlit as st
from datetime import datetime

# Set page layout
st.set_page_config(page_title="Upload", layout="centered")

# Custom CSS to style the page
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.5rem;
        color: #6c63ff;
        font-weight: bold;
        text-align: center;
    }
    .sub-title {
        font-size: 1rem;
        color: #A0A0A0;
        text-align: center;
    }
    .upload-container {
        border: 2px dashed #6c63ff;
        padding: 2rem;
        text-align: center;
        border-radius: 10px;
    }
    .upload-button {
        background-color: #6c63ff;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title and subtitle
st.markdown('<div class="main-title">Upload</div>', unsafe_allow_html=True)

# Batch name (automatically generated)
st.text_input("Batch Name:", value=f"Uploaded on {datetime.now().strftime('%m/%d/%y at %I:%M %p')}")

# Tags input
st.text_input("Tags:", placeholder="Search or add tags for images...")

# Upload section
st.markdown('<div class="upload-container">', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Drag and drop to upload, or:</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.file_uploader("Select Files", accept_multiple_files=True)
with col2:
    st.file_uploader("Select Folder", accept_multiple_files=True)

st.markdown("</div>", unsafe_allow_html=True)

# Supported formats section
st.write("Supported Formats")
st.write("Images in .jpg, .png, .bmp, .webp")
st.write("Annotations in 26 formats")
st.write("Videos in .mov, .mp4")
