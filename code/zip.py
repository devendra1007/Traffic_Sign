import zipfile
import os

def extract_zip(zip_path, extract_to_folder):
    if not os.path.exists(extract_to_folder):
        os.makedirs(extract_to_folder)

    # Extract the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_folder)
    
    print(f"Extracted {zip_path} to {extract_to_folder}")

# Example usage
zip_file_path = 'data/archive.zip' 
destination_folder = 'data'  
extract_zip(zip_file_path, destination_folder)
