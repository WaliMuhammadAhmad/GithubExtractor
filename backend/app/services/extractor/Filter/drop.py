import os
import shutil
from loggings import loggers

def check_json(folder_path):
    """
    Check if the given folder contains any JSON files.

    Args:
        folder_path (str): The path to the folder.

    Returns:
        bool: True if the folder contains at least one JSON file, False otherwise.
    """
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            return True
    return False

def delete_folder(folder_path):
    """
    Delete the specified folder.

    Args:
        folder_path (str): The path to the folder to be deleted.
    """

    try:
        shutil.rmtree(folder_path)
        print(f"Deleted folder: {folder_path}")
        log.info(f"Deleted folder : {folder_path}")
    except:
        log.error(f"Failed to delete folder : {folder_path}")

def process_folders(base_path):
    """
    Process each folder in the directory, deleting those that only contain 'log.txt'.

    Args:
        base_path (str): The path to the base dir containing the repo output folders.
    """
    
    total_folders = 0
    deleted_folders = 0

    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)

        if os.path.isdir(folder_path):
            total_folders += 1

            if not check_json(folder_path):
                log_files = [f for f in os.listdir(folder_path) if f == 'log.txt']
                if len(log_files) == 1 and len(os.listdir(folder_path)) == 1:
                    delete_folder(folder_path)
                    deleted_folders += 1

    print(f"Processed {total_folders} folders. Deleted {deleted_folders} folders that only contained 'log.txt'.")
    log.info(f"Total folders in '{base_path}' dir : {total_folders}")
    log.info(f"Deleted folders in '{base_path}' dir : {deleted_folders}")
    log.info(f"Remaining folders in '{base_path}' dir : {total_folders - deleted_folders}")

if __name__ == "__main__":

    log = loggers('logs/drop.log')

    base_path = "output"
    if os.path.exists(base_path):
        log.info(f"Drop empty folders in : {base_path} dir")
        process_folders(base_path)
    else :
        log.error(f"Path {base_path} does not exists in codespace.")

    log.warning(f"-- Only those folders are deleted which only has 'log.txt' in it --")