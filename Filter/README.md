# Filter the Scraper's output

This folder containes the python scripts to filter the data resulting scraper's output. This includes deleteing the empty folders, deleting junk like `log.txt` and then train test split.

## Content

- `.gitignore` - Specifies files and directories to be ignored by version control. Open it to see the content!

- `count.py` - A script to count the number of JSON files in directories.

- `distribute.py` - This script distributes files evenly across multiple folders.

- `drop.py` - A script to delete empty folders (which only have `log.txt` or `log.log`) producesd during the scraping process.

- `loggings.py` - A utility script to manage logging across the other scripts.

- `rm_log.py` - A script to delete all log.txt files from the dataset directories. If they are omited they will be part of the training data for model. These log files were generated during the scraping process and are not needed for model training.

- `split.py` - This script splits the dataset into training, evaluation and testing sets. It uses `**kwargs` for processing easily from termial. Rought right?

## Overview

All files uses the basic packages `os, shutil, argparse, random` which comes with python itself. so no need to explicity install them. `loggings.py` is used in every script for creating logs. All of the logs are placed in `./log` dir by default.

### count.py

Run this to verify the number of files or directories, ensuring that the distribution or filtering has been correctly applied. This is just a utility scripts not necessary to run. `dir_path` is necessary for starting:

```python
dir_path = "dataset"    # dir path

if os.path.exists(dir_path):
    log.info(f"Counting JSON files in : '{dir_path}' dir")
    process_folders(dir_path)
else :
    log.error(f"Path '{dir_path}' does not exists in codespace.")
```

### distribute.py

If you need to organize the dataset into multiple folders with a specific number of files per folder, use `distribute.py`. Huggingface requires that each folder should not contain files more then 10k, see the guid [here](https://huggingface.co/docs/hub/en/repositories-recommendations). So to push on huggingaface we must have to distribute the files into smaller numbers. This script creates sub-folders starting from 1,2,3... and each folder contains the number of the files specified in script. It uses `argparse` for easy running from terminal. 

```bash
python distribute.py --dir_path output --split_number 10000
```

However, `--dir_path` is *required*, `--split_number` args has a default value of `10000` you can change this accordingly.

### drop.py

Run this to remove any empty folders (which only have `log.txt` or `log.log`) in the directory. This cleans up the directory structure. To validate the empty folders it uses a function:

```python
def check_json(folder_path):
    """
    Args:
        folder_path (str): The path to the folder.

    Returns:
        bool: True if the folder contains at least one JSON file, False otherwise.
    """
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            return True
    return False
```

### rm_log.py

Run this to delete all `log files` from the dataset directories. These logs are not required for further processing and can be safely removed. By default, the scraper `./Scraper` uses `log.txt` for logging status for the repositories, so we are only removing `log.txt` files from the repository folders. To remove the `log.txt` it uses a function:

```python
def rm_log(folder_path):
    """
    Args:
        folder_path (str): The path to the folder.
    """

    log_file_path = os.path.join(folder_path, 'log.txt')
    if os.path.exists(log_file_path):
        os.remove(log_file_path)
        log.info(f"Removed 'log.txt' from {folder_path}")
    else:
        log.error(f"{folder_path} doesnt have 'log.txt'")
```

### split.py

This script is used to divide the dataset into train, eval test sets. It creates a new folder, shuffle the dataset before split and then creates these sub-folder `['eva','train','test']` in that dir. It uses `argparse` for easy running from terminal. 

```bash
python split.py --output_path data --test_split 0.2 --eval_split 0.2 --shuffle True
```

However, above shown are the default args you can change this accordingly.

### loggings.py

Logging is provided by `loggings.py` to help track the operations performed by each script. It creats a `./log` dir in codespace and places all the logs from other scripts there. The logs statuses `[info, warning, error]` are according to state. 