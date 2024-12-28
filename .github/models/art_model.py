import os
from PIL import Image
import matplotlib.pyplot as plt

# Load the image
def load_image(image_path):
    """
    Loads and displays the given image.

    Args:
        image_path (str): Path to the image file.

    Returns:
        PIL.Image.Image: The loaded image.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    image = Image.open(image_path)
    return image


# Display the image
def display_image(image):
    """
    Displays the given image using matplotlib.

    Args:
        image (PIL.Image.Image): The image to display.
    """
    plt.imshow(image)
    plt.axis("off")
    plt.title("Manga Profile Picture Example")
    plt.show()


# Main execution
if __name__ == "__main__":
    # Path to the image
    image_path = "image.png"  # Make sure the file is in the same directory or update the path

    try:
        # Load and display the image
        manga_image = load_image(image_path)
        display_image(manga_image)
    except Exception as e:
        print(f"Error: {e}")
