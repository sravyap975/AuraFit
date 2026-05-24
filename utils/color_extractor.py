from colorthief import ColorThief
import tempfile


def extract_colors(uploaded_file, color_count=5):

    # Reset file pointer
    uploaded_file.seek(0)

    # Create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:

        temp_file.write(uploaded_file.getvalue())

        temp_file_path = temp_file.name

    # Extract colors
    color_thief = ColorThief(temp_file_path)

    palette = color_thief.get_palette(
        color_count=color_count
    )

    return palette