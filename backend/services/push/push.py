from backend.app.utils.loggings import loggers

def push(repo,local_dir):
    """
    This function authenticates the user, pushes local directories to a huggingface repository, and logs the process.

    Args:
        repo_id (str): The name of the huggingface repository to push the files to.
        clone_path (str): The local clone path of the huggingface repository.

    Returns:
        None
    """

    log = loggers('logs/push.log')
    log.info(f"{local_dir} pushing to huggingface...")
    try:
        repo.push_to_hub(commit_message=f"dataset uploaded")
        log.info(f"{local_dir} pushed to huggingface.")
        print("Successfully pushed to huggingface.")

    except:
        print("Push huggingface failed!")
        log.error("Push huggingface failed! \n This is either the repo is not created or failed to clone.")