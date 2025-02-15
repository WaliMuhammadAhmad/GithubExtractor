import os
import shutil
import argparse
from loggings import loggers

def distribute(dir_path, split=1000):
    """
    Distribute JSON files into equally sized folders under the given directory.

    Args:
        dir_path (str): The path to the directory containing JSON files.
        split (int): The number of JSON files to place in each new folder.
    """
    log = loggers('logs/dist.log')

    all_json_files = [os.path.join(dir_path, file_name) for file_name in os.listdir(dir_path) if file_name.endswith(".json")]
    total_files = len(all_json_files)
    log.info(f"Number of JSON files in '{dir_path}' : {total_files}")
    print(f"Total JSON files found: {total_files}")

    if total_files <= split:
        print(f" {total_files} < {split}. No splitting required.")
        log.warning(f" {total_files} < {split}. No splitting required.")
        return

    folder_index = 1
    file_count = 0

    for i, json_file in enumerate(all_json_files):
        if file_count == 0:
            new_folder_path = os.path.join(dir_path, str(folder_index))
            os.makedirs(new_folder_path, exist_ok=True)
            print(f"Created folder: {new_folder_path}")

        shutil.move(json_file, os.path.join(new_folder_path, os.path.basename(json_file)))
        file_count += 1

        if file_count >= split:
            folder_index += 1
            file_count = 0

    print(f"Distributed {total_files} JSON files into {folder_index} folders.")
    log.info(f"Distributed {total_files} JSON files into {folder_index} folders.")

def parse_args():
    """
    Parse the args passed from the command line
    """
    parser = argparse.ArgumentParser(description="Distribute JSON files into subfolders with a specified number of files per folder.")

    parser.add_argument(
        '--dir_path', 
        type=str, 
        required=True, 
        help="The path to the directory containing JSON files."
    )
    parser.add_argument(
        '--split_number', 
        type=int, 
        default=1000, 
        help="Number of files per split folder (HF requiress 10k per folder)"
    )

    return vars(parser.parse_args())

if __name__ == "__main__":
    
    args = parse_args()
    dir_path = args['dir_path']
    split_number = args['split_number']
    
    distribute(dir_path, split_number)