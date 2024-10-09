import streamlit as st
import os
from datetime import datetime
from pathlib import Path

# Sidebar setup
st.sidebar.title("WORK")
st.sidebar.image("C:\Users\Panch\Documents\Streamlitapp\imagenes\Screenshot 2024-07-19 165847.png")  # Replace with an actual image path if needed
st.sidebar.write("platte")
st.sidebar.write("Object Detection")

st.sidebar.title("DATA")
sections = ["Settings", "Upload Data", "Annotate", "Dataset", "Analytics", "Generate"]
for section in sections:
    st.sidebar.button(section)

# Main content for Upload Data section
st.title("Upload")
st.write(f"Batch Name: Uploaded on {datetime.now().strftime('%m/%d/%y at %I:%M %p')}")
tags = st.text_input("Tags:", "Search or add tags for images...")

st.markdown(
    """
    <div style="text-align: center; margin-top: 20px;">
        <h3>Drag and drop to upload, or:</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

# File uploader
uploaded_files = st.file_uploader("Select Files", type=["jpg", "png", "bmp", "webp"], accept_multiple_files=True)

# Folder scanning
folder_path = st.text_input("Folder Path", placeholder="Enter folder path to scan for images")

if folder_path:
    folder = Path(folder_path)
    if folder.exists() and folder.is_dir():
        image_files = [str(file) for file in folder.glob("*.jpg")]
        image_files += [str(file) for file in folder.glob("*.png")]
        image_files += [str(file) for file in folder.glob("*.bmp")]
        image_files += [str(file) for file in folder.glob("*.webp")]
        
        st.write(f"Found {len(image_files)} images in folder:")
        for img in image_files:
            st.write(img)
    else:
        st.error("Invalid folder path.")

st.markdown(
    """
    <div style="text-align: center; margin-top: 40px;">
        <button style="color: #8B00FF;">Supported Formats</button>
        <p>Images: .jpg, .png, .bmp, .webp | Videos: .mov, .mp4</p>
    </div>
    """,
    unsafe_allow_html=True,
)
