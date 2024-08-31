import zipfile
import os
import json

def process_json_files(source_folder, target_folder):
    # Iterate through all files and directories in the source folder
    for root, dirs, files in os.walk(source_folder):
        # Create corresponding directories in the target folder
        relative_path = os.path.relpath(root, source_folder)
        target_root = os.path.join(target_folder, relative_path)
        os.makedirs(target_root, exist_ok=True)

        for filename in files:
            # Check if the file is a JSON file
            if filename.endswith(".json"):
                file_path = os.path.join(root, filename)

                # Read the content of the JSON file
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)

                # Extract only the "body" fields of "test_case" and "focal_method"
                new_data = {
                    # "test_class_name": data.get("test_class", {}).get("identifier", ""),
                    # "method_name": data.get("test_case", {}).get("identifier", ""),
                    "focal_method_body": data.get("focal_method", {}).get("body", ""),
                    "test_case_body": data.get("test_case", {}).get("body", "")
                }

                # Define the new file path
                new_file_path = os.path.join(target_root, filename)

                # Write the new data to a new JSON file in the target folder
                with open(new_file_path, "w", encoding="utf-8") as new_file:
                    json.dump(new_data, new_file, indent=4)

                print(f"Processed {filename} and saved to {new_file_path}")


# Define the folder containing your JSON files
source_folder_path = "/content/test_case_jsons"

# Define the folder where new JSON files will be saved
target_folder_path = "/content/extracted_data"

# Process the JSON files
process_json_files(source_folder_path, target_folder_path)

# Zip the folder
!zip -r /content/extracted_data.zip /content/extracted_data

# Download the zip file
from google.colab import files
files.download("/content/extracted_data.zip")
