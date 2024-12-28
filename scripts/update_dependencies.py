import os

def update_dependencies():
    """
    Updates Python dependencies based on requirements.txt.
    """
    print("Updating dependencies...")
    os.system("pip install --upgrade -r ../requirements.txt")  # Adjust path if requirements.txt is elsewhere
    print("All dependencies are up to date.")

if __name__ == "__main__":
    update_dependencies()
