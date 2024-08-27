from huggingface_hub import login
from access_token import auth
from loggings import loggers
from get_repo import get_repo
import shutil
import os

log = loggers('logs/push.log')

def move_folder(source_folder, destination_folder):
    """
    Moves a folder from source to destination.

    Args:
        source_folder (str): The path to the folder you want to move.
        destination_folder (str): The path to the destination where the folder should be moved.
    """
    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Move the folder
        shutil.move(source_folder, destination_folder)
        log.info(f"Moved folder '{source_folder}' to '{destination_folder}' successfully.")
    except Exception as e:
        print(f"Failed to move folder: {source_folder}")
        log.error(f"Failed to move folder: {str(e)}")

def push(repo_id,local_path, clone_path):
    """
    This function authenticates the user, 
    pushes local directories to a huggingface
    repository, and logs the process.

    Args:
        repo_id (str): The name of the huggingface repository to push the files to.
        local_path (str): The local directory containing folders to be moved and 
                            pushed to the huggingface repository.
        clone_path (str): The local clone path of the huggingface repository.

    Returns:
        None
    """

    try:
        login(auth(),add_to_git_credential=True)
        log.info("huggingface login successful!")
        log.warning("add_to_git_credential are set to 'True'")

        try:
            repo = get_repo(clone_path,repo_id)
            folders = os.listdir(local_path)
            for dir in folders:
                log.info(f"Moving {dir} to {clone_path}...")
                move_folder(f"{local_path}/{dir}",clone_path)
                log.info(f"{dir} pushed to huggingface.")
                repo.push_to_hub(commit_message=f"{dir} uploaded")
            
            print("Successfully pushed to huggingface.")
            log.info(f"{repo_id} pushed to huggingface.")

        except:
            print("Push huggingface failed!")
            log.error("Push huggingface failed! \n This is either the repo is not created or failed to clone.")
    except:
        log.error("huggingface login failed!")
        return None

if __name__ == "__main__":

    local_path = "dataset"
    repo_name = "raw_dataset"
    repo_id = f'CodexAI/{repo_name}'

    clone_path = repo_name

    if (local_path and clone_path):
        log.info(f"Pushing {local_path} to {repo_id}...")
        push(repo_id,local_path, clone_path)
    else:
        log.error(f"Pushing failed! '{clone_path}' and '{local_path}' are empty!")
        print(f"{repo_name} and {local_path} are required!")