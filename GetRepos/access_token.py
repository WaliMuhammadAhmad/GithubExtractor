from dotenv import load_dotenv
from github import Github
from github import Auth
import os

try:
    load_dotenv()  # take environment variables from .env.
    github_token = os.getenv("GITHUB_TOKEN")

    try:
        auth = Auth.Token(github_token)
        g = Github(auth=auth)
        usr = g.get_user()
        print(usr.name) # if your token is valid then this should print your name
    except:
        print(f'[{github_token}] is not valid')
except:
    print(f"failed to load {github_token}, either '.env' or 'dotenv' package is missing!")