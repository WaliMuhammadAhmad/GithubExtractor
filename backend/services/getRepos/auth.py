from github import Github, Auth
from dotenv import load_dotenv
import os

_g_instance: Github | None = None
_github_token: str | None = None

def github() -> tuple[Github, str] | tuple[None, None]:
    """
    Authenticates the GitHub access token stored in .env and returns a reusable Github instance.

    Returns:
        tuple[Github, str]: The Github instance and token if authentication is successful.
        tuple[None, None]: If authentication fails.
    """
    global _g_instance, _github_token
    
    # Return existing instance if already authenticated
    if _g_instance is not None and _github_token is not None:
        return _g_instance, _github_token
    
    try:
        load_dotenv()
        github_token = os.getenv("GITHUB_TOKEN")
        
        if not github_token:
            print("Github token not found in the environment variables.")
            return None, None
        
        auth = Auth.Token(github_token)
        g = Github(auth=auth)

        usr = g.get_user()
        print(f"Authenticated as: {usr.name}")

        _g_instance = g
        _github_token = github_token
        return g, github_token
    
    except Exception as e:
        print(f"Failed to Authenticate! Error: {str(e)}")
        return None, None

if __name__ == "__main__":
   github()