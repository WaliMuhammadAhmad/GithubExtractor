import json
import os

def process_json_files(source_folder, target_folder):
    """
    Processes JSON files from the source folder, extracting specific fields, and saves the processed
    data to the target folder while maintaining the directory structure.

    Args:
        source_folder (str): The directory containing the original JSON files.
        target_folder (str): The directory where processed JSON files will be saved.

    Returns:
        None
    """

    for root, dirs, files in os.walk(source_folder):
        # Create corresponding directories in the target folder
        relative_path = os.path.relpath(root, source_folder)
        target_root = os.path.join(target_folder, relative_path)
        os.makedirs(target_root, exist_ok=True)

        for filename in files:
            if filename.endswith(".json"):
                file_path = os.path.join(root, filename)

                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)

                new_data = {
                    "focal_method": data.get("focal_method", {}).get("body", ""),
                    "test_case": data.get("test_case", {}).get("body", "")
                }

                new_file_path = os.path.join(target_root, filename)
                with open(new_file_path, "w", encoding="utf-8") as new_file:
                    json.dump(new_data, new_file, indent=4)

                print(f"Processed {filename} and saved to {new_file_path}")

if __name__ == "__main__":

    name = "eval"   # ['eval','test','train']

    input_path = f"dataset/{name}"
    output_path = f"prep/{name}"

    process_json_files(input_path, output_path)