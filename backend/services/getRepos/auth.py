from github import Github, Auth
from dotenv import load_dotenv
import os

def github():
    """
    This function authenticates the github access token stored in the (.env)

    Args:
        None

    Returns:
        g (Github): The github object if authentication is successful. && github_token (str): The github access token if authentication is successful.
        None: If authentication fails.
    """
    try:
        load_dotenv()
        github_token = os.getenv("GITHUB_TOKEN")

        if github_token:
            try:
                auth = Auth.Token(github_token)
                g = Github(auth=auth)
                usr = g.get_user()
                print(f"Authenticated as : {usr.name}")
                return g, github_token
            except Exception as e:
                print(f"Token [{github_token}] is not valid")
        else:
            print("Github token not found in the environment variables.")
    except Exception as e:
        print(f"Failed to Authenticate! either '.env' is empty or missing \n Error: {str(e)}")

if __name__ == "__main__":
    github()