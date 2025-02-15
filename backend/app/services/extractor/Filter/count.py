import os
from loggings import loggers

def count_json_files(path):
    """
    Count the number of JSON files in the given folder.

    Args:
        path (str): The path to the folder.

    Returns:
        int: The number of JSON files in the folder.
    """
    try:
        json_files = [f for f in os.listdir(path) if f.endswith(".json")]
        return len(json_files)
    except:
        log.error(f"Failed to count in : {path} dir")

def process_folders(dir_path):
    """
    Process each folder in the base directory, counting the JSON files in each.

    Args:
        dir_path (str): The path to the base directory containing the repo folders.
    """
    total_json_files = 0

    # Iterate over each folder in the base directory
    for folder_name in os.listdir(dir_path):
        folder_path = os.path.join(dir_path, folder_name)

        if os.path.isdir(folder_path):
            json_count = count_json_files(folder_path)
            total_json_files += json_count
            print(f"Folder '{folder_name}' contains {json_count} JSON file(s).")

    print(f"\nTotal JSON files in all folders: {total_json_files}")
    log.info(f"Total JSON files in '{dir_path}' dir : {total_json_files} ")

if __name__ == "__main__":
    
    log = loggers('logs/count.log')

    dir_path = "dataset"    # dir path to be counted
    
    if os.path.exists(dir_path):
        log.info(f"Counting JSON files in : '{dir_path}' dir")
        process_folders(dir_path)
    else :
        log.error(f"Path '{dir_path}' does not exists in codespace.")