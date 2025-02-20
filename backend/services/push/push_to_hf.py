from huggingface_hub import login, Repository
import shutil
import os

def move_folder(source_folder, destination_folder):

    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Move the folder
        shutil.move(source_folder, destination_folder)
        print(f"Moved folder '{source_folder}' to '{destination_folder}' successfully.")
    except Exception as e:
        print(f"Failed to move folder: {source_folder}")


login('HF_TOKEN',add_to_git_credential=True)

local_path = "dataset"
repo_name = "dataset"
repo_id = f'{repo_name}'
clone_path = repo_name

repo = Repository(local_dir=clone_path, clone_from=f"https://huggingface.co/datasets/{repo_id}")
repo.git_pull()

os.listdir(clone_path)
move_folder(local_path,clone_path)
repo.push_to_hub(commit_message=f"{local_path} uploaded")
shutil.rmtree(repo_name)