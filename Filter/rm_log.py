import os
from loggings import loggers

def rm_log(folder_path):
    """
    Remove the 'log.txt' file from the given folder if it exists.

    Args:
        folder_path (str): The path to the folder.
    """
    log_file_path = os.path.join(folder_path, 'log.txt')
    if os.path.exists(log_file_path):
        os.remove(log_file_path)
        log.info(f"Removed 'log.txt' from {folder_path}")
    else:
        log.error(f"{folder_path} doesnt have 'log.txt'")

def process_folders(path):
    """
    Process each folder in the base directory, removing 'log.txt' files from folders containing JSON files.

    Args:
        path (str): The path to the base directory containing the repo folders.
    """
    total_folders_processed = 0

    for folder_name in os.listdir(path):
        folder_path = os.path.join(path, folder_name)

        if os.path.isdir(folder_path):
            if any(f.endswith('.json') for f in os.listdir(folder_path)):
                rm_log(folder_path)
                total_folders_processed += 1

    print(f"Processed {total_folders_processed} folders.")

if __name__ == "__main__":
    
    log = loggers('logs/rm_log.log')

    dir_path = "output"
    if os.path.exists(dir_path):
        log.info(f"Removing 'log.txt' from : '{dir_path}' dir")
        process_folders(dir_path)
    else :
        log.error(f"Path '{dir_path}' does not exists in codespace.")
