import os
import shutil

CACHE_DIR = "../cache"  # Update to the actual cache directory

def clear_cache():
    """
    Clears cached files and temporary data.
    """
    if os.path.exists(CACHE_DIR):
        print(f"Clearing cache at {CACHE_DIR}...")
        shutil.rmtree(CACHE_DIR)
        os.makedirs(CACHE_DIR)  # Recreate an empty cache folder
        print("Cache cleared.")
    else:
        print("No cache found. Skipping.")

if __name__ == "__main__":
    clear_cache()
