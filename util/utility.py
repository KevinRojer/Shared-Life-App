import os


def ensure_directory_exists(filepath):
    """Ensure the directory of the filepath exists; if not, create it."""
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)