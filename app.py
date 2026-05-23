import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="AuraFit", page_icon="👕")

# Title
st.title("AuraFit 👕✨")
st.write("AI-powered outfit matching assistant")

# File uploader
uploaded_file = st.file_uploader(
    "Upload a clothing image",
    type=["jpg", "jpeg", "png"]
)

# Display image if uploaded
if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Clothing Item",
        use_container_width=True
    )

    st.success("Image uploaded successfully!")