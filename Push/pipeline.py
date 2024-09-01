import argparse
from get_repo import get_repo
from preprocess import process_json_files
from push import push

def parse_args():
    """
    Parse the args passed from the command line.
    
    Args:
        None

    Returns:
        vars(parser.parse_args()) (dict): Containing the parsed arguments with their corresponding values.
    """
    
    parser = argparse.ArgumentParser(description="Pipeline to make this whole process auto.")

    parser.add_argument(
        '--repo_name',
        type=str, 
        required=True, 
        help="Name of the repo to make"
    )
    parser.add_argument(
        '--clone_dir', 
        type=str, 
        default="dataset", 
        help="Path of the dir where to clone the repo"
    )
    parser.add_argument(
        '--local_dir', 
        type=str, 
        default="data", 
        help="Path of the local dir which has the dataset"
    )

    return vars(parser.parse_args())

if __name__ == "__main__" :

    args = parse_args()
    repo_name = args['repo_name']
    clone_dir = args['clone_dir']
    local_dir = args['local_dir']

    repo_id = f"CodexAI/{repo_name}"

    repo = get_repo(clone_dir,repo_id)
    process_json_files(local_dir,clone_dir)
    push(repo,local_dir)