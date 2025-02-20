from huggingface_hub import HfApi, HfFolder
from github import Github, Auth
from dotenv import load_dotenv
from loggings import loggers
import argparse
import os

def github():
    """
    This function authenticates the github access token stored in the (.env)

    Args:
        None

    Returns:
        github_token (str): The github access token if authentication is successful.
        None: If authentication fails.
    """
    try:
        load_dotenv()
        github_token = os.getenv("GITHUB_TOKEN")

        log = loggers("logs/auth.log")
        log.info("Authenticating Github token...")

        if github_token:
            try:
                auth = Auth.Token(github_token)
                g = Github(auth=auth)
                usr = g.get_user()
                print(usr.name)
                log.warning(f"Authenticated as : {usr.name}")
                return github_token
            except Exception as e:
                print(f"Token [{github_token}] is not valid")
                log.error(f"Token [{github_token}] is not valid: {str(e)}")
        else:
            print("Github token not found in the environment variables.")
            log.error(f"Failed to Authenticate! '.env' is empty \n Error: {str(e)}")
    except Exception as e:
        print(f"Failed to load the token")
        log.error(f"Failed to Authenticate! either '.env' is empty or missing \n Error: {str(e)}")

def hf():
    """
    This function authenticates the user with huggingface using a token stored in the (.env)

    Args:
        None

    Returns:
        hf_token (str): The huggingface token if authentication is successful.
        None: If authentication fails.
    """
    
    try:
        load_dotenv()
        hf_token = os.getenv("HF_TOKEN")

        log = loggers("logs/auth.log")
        log.info("Authenticating HF token...")

        if hf_token:
            try:
                HfFolder.save_token(hf_token)
                api = HfApi()
                user_info = api.whoami()
                print(user_info['name'])
                log.warning(f"Authenticated as : {user_info['name']}")
                return hf_token
            except Exception as e:
                print(f"Token [{hf_token}] is not valid")
                log.error(f"Token [{hf_token}] is not valid: {str(e)}")
        else:
            print("huggingface token not found in the environment variables.")
            log.error(f"Failed to Authenticate! '.env' is empty \n Error: {str(e)}")
    except Exception as e:
        print(f"Failed to load the token")
        log.error(f"Failed to Authenticate! either '.env' is empty or missing \n Error: {str(e)}")

def parse_args():
    """
    This function parses command line arguments.

    Args:
        None

    Returns:
        args: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description="Authenticate tokens for GitHub and HuggingFace.")
    parser.add_argument("--service", type=str, choices=["github", "hf"], required=True, help="The service to authenticate (github or hf).")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    if args.service == "github":
        github()
    elif args.service == "hf":
        hf()
    else:
        print("Invalid service. Please choose either 'github' or 'hf'.")