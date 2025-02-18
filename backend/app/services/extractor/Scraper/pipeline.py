import subprocess
import argparse
import pandas as pd
from check import check_so_file
from loggings import loggers

def automate_find_map_test_cases(csv_file, start, end, tmp, output):
    '''
    As it's name tells, this function automate the process by runing the find_map_test_cases.py
    script for fixed range, taking input params from a csv file in the dir. For running this script
    the csv file is requird to have ID = project_id, URL = html_url and Name = repo_name of Repo
    '''
    log = loggers('logs/pipeline.log')

    df = pd.read_csv(csv_file)
    df_subset = df[start:end]
    log.info(f"Reading {csv_file} from {start} to {end}")
    
    for index, row in df_subset.iterrows():
        repo_id = str(row['ID'])  # subprocess command requires the kwargs to be string
        repo_url = row['URL']
        repo_name = row['Name']

        print(f"Processing repository: {repo_name}")
        
        # command to run find_map_test_cases.py
        command = [
            "python", 
            "find_map_test_cases.py", 
            "--repo_url", repo_url, 
            "--repo_id", repo_id,
            "--tmp", tmp,
            "--output", output,
        ]
        
        # Execute the command using subprocess
        try:
            log.info(f"Running command for Repo : [{repo_name}] \n {command}")
            result = subprocess.run(command, check=True)
            print(f"Finished Repo: {repo_name}")
            print('-'*20)
            log.info(f"Processing finished for Repo : [{repo_name}] \n Result at {output}{repo_id}")
        except subprocess.CalledProcessError as e:
            print(f"Error running command for repo_id {repo_id}: {e}")
            log.error(f"Error running command for : [{repo_name}]: {e}")

def parse_args():
	"""
	Parse the args passed from the command line
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"--csv_path", 
		type=str, 
		default="./data/RepoData.csv",
		help="Path of the csv file which has the Github Repo's Info",
	)
	parser.add_argument(
		"--start",
		type=int,
		default=0,
		help="Start range for the method and test extraction of Repos",
	)
	parser.add_argument(
		"--end",
		type=int,
		default=1,
		help="End range for the method and test extraction of Repos",
	)
	parser.add_argument(
		"--tmp",
		type=str,
		default="./tmp",
		help="Path to a temporary folder used for cloning the repos",
	)
	parser.add_argument(
		"--output",
		type=str,
		default="./output/",
		help="Path to the output folder",
	)

	return vars(parser.parse_args())

def main():
    args = parse_args()
    csv_path = args['csv_path']
    start = args['start']
    end = args['end']
    tmp = args['tmp']
    output = args['output']
    
    if check_so_file():
        automate_find_map_test_cases(csv_path, start, end, tmp, output)
    else:
        print("Please run the check.py script first to check the existence of the required .so files!")

if __name__ == '__main__':
	main()