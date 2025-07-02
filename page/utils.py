import os
import uuid

def generate_unique_filepath(instance, filename, base_path='uploads/'):
    """
    Generate a unique filename for uploaded files.
    
    Args:
        instance: The model instance that is being saved.
        filename: The original filename of the uploaded file.
        base_path (str): The base directory where the file will be saved.
    
    Returns:
        str: A unique filename based on the original filename and a UUID.
    """
    ext = os.path.splitext(filename)[-1]  # Get the file extension
    unique_filename = f"{uuid.uuid4().hex}.{ext}"

    return os.path.join(base_path, unique_filename)