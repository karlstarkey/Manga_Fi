import os
from art_model import load_image, display_image

def generate_sample():
    """
    Generates a sample manga PFP and displays it.
    """
    SAMPLE_IMAGE_PATH = "../image.png"  # Replace with actual sample image path

    if os.path.exists(SAMPLE_IMAGE_PATH):
        print("Loading sample image...")
        image = load_image(SAMPLE_IMAGE_PATH)
        display_image(image)
        print("Sample generated successfully!")
    else:
        print(f"Sample image not found at {SAMPLE_IMAGE_PATH}.")

if __name__ == "__main__":
    generate_sample()
