from colorthief import ColorThief
from PIL import Image
import tempfile


def extract_colors(image_file):

    # Open image
    image = Image.open(image_file)

    # Resize image
    image = image.resize((300, 300))

    # Crop center area
    width, height = image.size

    left = width * 0.2
    top = height * 0.2
    right = width * 0.8
    bottom = height * 0.8

    image = image.crop((left, top, right, bottom))

    # Save temporary image
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")

    image.save(temp_file.name)

    # Extract palette
    color_thief = ColorThief(temp_file.name)

    palette = color_thief.get_palette(color_count=5)

    return palette