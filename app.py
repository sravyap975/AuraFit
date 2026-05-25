from utils.matcher import get_outfit_recommendations
import streamlit as st
from PIL import Image

from utils.color_extractor import extract_colors

# Page config
st.set_page_config(
    page_title="AuraFit",
    page_icon="👕"
)

# Title
st.title("AuraFit 👕✨")
st.write("AI-powered outfit matching assistant")
# Fashion aesthetic selector
aesthetic = st.selectbox(
    "Choose your fashion aesthetic",
    [
        "Streetwear",
        "Old Money",
        "Korean Casual",
        "Minimalist"
    ]
)

# Upload section
uploaded_file = st.file_uploader(
    "Upload a clothing image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Display image
    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Clothing Item",
        use_container_width=True
    )

    st.success("Image uploaded successfully!")

    # Extract colors
    uploaded_file.seek(0)

    colors = extract_colors(uploaded_file)

    st.subheader("Detected Color Palette 🎨")

    # Display colors
    cols = st.columns(len(colors))

    for idx, color in enumerate(colors):

        hex_color = '#%02x%02x%02x' % color

        cols[idx].markdown(
            f"""
            <div style="
                width: 80px;
                height: 80px;
                background-color: {hex_color};
                border-radius: 10px;
                border: 2px solid white;
            ">
            </div>

            <p style='text-align:center;'>{hex_color}</p>
            """,
            unsafe_allow_html=True
        )
            # Dominant color
    dominant_color = colors[0]

    dominant_hex = '#%02x%02x%02x' % dominant_color

    # Recommendations
    recommendations = get_outfit_recommendations(
    dominant_hex,
    aesthetic
)

    st.subheader("Outfit Recommendations 👗")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Tops")
        for item in recommendations["tops"]:
            st.write(f"• {item}")

    with col2:
        st.markdown("### Bottoms")
        for item in recommendations["bottoms"]:
            st.write(f"• {item}")

    with col3:
        st.markdown("### Shoes")
        for item in recommendations["shoes"]:
            st.write(f"• {item}")