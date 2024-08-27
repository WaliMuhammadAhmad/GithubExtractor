from huggingface_hub import login
from huggingface_hub import Repository
from huggingface_hub import create_repo
# from huggingface_hub import HfApi
from access_token import auth
import os

def get_repo(clone_path,repo_id):
    """
    THis function authenticates the user with huggingface, 
    creates or retrieves a repository, and clones it locally.

    Args:
        clone_path (str): The local directory path where the repository will be cloned.
        repo_id (str): The name of the repository to create or fetch from huggingface.

    Returns:
        repo (Repository or None): The cloned repository object if successful, or None if an error occurs.
    """

    try:
        login(auth(),add_to_git_credential=True)
        print("huggingface login successful!")

        try:
            repo_url = create_repo(repo_id, repo_type="dataset", private=True,exist_ok=True)
            print(f"{repo_id} created successfully! Now cloning it to {clone_path}...")
            os.makedirs(clone_path,exist_ok=True)
            repo = Repository(local_dir=clone_path, clone_from=repo_url)
            repo.git_pull()
            print("Clone finished!")
            return repo
        
            # Alternative approach using HfApi:
            # Uncomment the following lines and comment out the git lines above to use HfApi for uploading.
            
            # api = HfApi()
            # os.chdir(path)

            # api.upload_folder(
            #   folder_path=path,
            #   repo_id=repo_id,
            #   repo_type="dataset",
            # )

        except:
            print(f"fetch repo failed from : {repo_url}")
            return None

    except:
        print("huggingface login failed!")
        return None

    return repo

if __name__ == "__main__":
    get_repo()