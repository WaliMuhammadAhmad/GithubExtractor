from dotenv import load_dotenv
from github import Github
from github import Auth
import os

def auth():
    """
    This function authenticates the github access token stored in the (.env)

    Returns:
        github_token (str): The github access token if authentication is successful.
        None: If authentication fails.
    """
    try:
        load_dotenv()  # take environment variables from .env.
        github_token = os.getenv("GITHUB_TOKEN")

        try:
            auth = Auth.Token(github_token)
            g = Github(auth=auth)
            usr = g.get_user()
            print(usr.name) # if your token is valid then this should print your name
            return github_token
        except:
            print(f'[{github_token}] is not valid')
            return
    except:
        print(f"failed to load {github_token}, either '.env' or 'dotenv' package is missing!")
        return
    
if __name__ == "__main__":
    auth()