import os
from huggingface_hub import HfApi, HfFolder
from dotenv import load_dotenv
from loggings import loggers

def auth():
    """
    This function authenticates the user with huggingface using a token stored in the (.env)

    Args:
        None

    Returns:
        hf_token (str): The huggingface token if authentication is successful.
        None: If authentication fails.
    """
    
    try:
        load_dotenv()  # Load environment variables from .env file
        hf_token = os.getenv("HF_TOKEN")

        log = loggers("logs/auth.log")
        log.info("Authenticating HF token...")

        if hf_token:
            try:
                HfFolder.save_token(hf_token)
                api = HfApi()
                user_info = api.whoami()
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

if __name__ == "__main__":
    auth()