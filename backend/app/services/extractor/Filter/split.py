import os
import shutil
import random
import argparse
from loggings import loggers

def split_dataset(json_files,test_split, eval_split, shuffle,output_dir = './data'):
    """
    Split the dataset into training, test, and evaluation sets.

    Args:
        json_files (list): List of paths to JSON files.
        test_split (float): Proportion of data to allocate to the test set.
        eval_split (float): Proportion of data to allocate to the evaluation set.
        shuffle (bool): Whether to shuffle the dataset before splitting.
        output_dir = './data' : Path where the dataset folders will be created. You can also change the default param.
    """
    log = loggers('logs/split.log')

    if shuffle:
        random.shuffle(json_files)
        print("Shuffled the dataset.")
        log.info("Dataset Shuffled")
    else:
        log.warning(f"Dataset Shuffled is set to : {shuffle}.Set 'True' to shuffle the dataset which is recommended.")


    total_files = len(json_files)
    test_count = int(total_files * test_split)
    eval_count = int(total_files * eval_split)
    train_count = total_files - test_count - eval_count

    # Create directories
    train_dir = f"{output_dir}/train"
    test_dir = f"{output_dir}/test"
    eval_dir = f"{output_dir}/eval"
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    os.makedirs(eval_dir, exist_ok=True)
    log.info(f"Sub-folder's [{train_dir}],[{test_dir}],[{eval_dir}] created at : '{output_dir}'")

    # Split the dataset
    train_files = json_files[:train_count]
    test_files = json_files[train_count:train_count + test_count]
    eval_files = json_files[train_count + test_count:]

    print(f"Total files: {total_files}")
    print(f"Training: {len(train_files)}, Test: {len(test_files)}, Eval: {len(eval_files)}")

    # Move files to respective directories
    try:
        for file in train_files:
            shutil.move(file, os.path.join(train_dir, os.path.basename(file)))

        for file in test_files:
            shutil.move(file, os.path.join(test_dir, os.path.basename(file)))

        for file in eval_files:
            shutil.move(file, os.path.join(eval_dir, os.path.basename(file)))

        print(f"Files moved to train, test, and eval directories.")
    except:
        log.error("Files moved failed!")
    
    # Logging
    log.info(f"Total files in dataset: {total_files}")
    log.info(f"Total files in train: {len(os.listdir(train_dir))}")
    log.info(f"Total files in test: {len(os.listdir(test_dir))}")
    log.info(f"Total files in eval: {len(os.listdir(eval_dir))}")

def gather_json_files(path):
    """
    Gather all JSON files from the dataset.

    Args:
        path (str): Path to the base directory containing JSON files.

    Returns:
        list: List of paths to JSON files.
    """
    json_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))
    return json_files

def parse_args():
	"""
	Parse the args passed from the command line
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"--output_path", 
		type=str, 
		default="./data",
		help="Path to the dataset output directory.",
	)
	parser.add_argument(
		"--test_split",
		type=float,
		default=0.2,
		help="Proportion of data to allocate to test set.",
	)
	parser.add_argument(
		"--eval_split",
		type=float,
		default=0.2,
		help="Proportion of data to allocate to evaluation set.",
	)
	parser.add_argument(
		"--shuffle",
		type=bool,
		default=True,
		help="Shuffle the dataset before splitting.",
	)

	return vars(parser.parse_args())

def main():
    args = parse_args()
    output_path = args['output_path']
    test_split = args['test_split']
    eval_split = args['eval_split']
    shuffle = args['shuffle']

    input_path = 'output'

    json_files = gather_json_files(input_path)
    split_dataset(json_files,test_split,eval_split,shuffle,output_path)

if __name__ == "__main__":
    main()