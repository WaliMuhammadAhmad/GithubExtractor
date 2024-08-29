from github import Github, Auth
import pandas as pd
import shutil
import os
from access_token import auth

def get_repo_details(output_dir='data'):
    """
    Retrieves details of public Java repositories and saves them to a CSV file.

    Args:
        output_dir (str): The dir where the CSV file will be saved. Defaults to 'data'.

    Returns:
        None
    """

    auth = Auth.Token(auth())
    g = Github(auth=auth)

    query = "language:java created:>=2024-01-01"

    repos = g.search_repositories(query=query)
    print(f"{repos.totalCount} Java repositories found!")

    data = extract(repos)
    data.to_csv('RepoData.csv', index=False)

    os.makedirs(output_dir, exist_ok=True)
    shutil.copy('RepoData.csv', output_dir)
    print(f'Data extracted and saved successfully at {output_dir}!')

    g.close()

def extract(java_repos):
    """
    Extracts details from the list of Java repositories and returns them as a DataFrame.

    Args:
        java_repos (PaginatedList): A list of Java repositories returned by the GitHub API.

    Returns:
        repos_df (DataFrame): A DataFrame containing the details of the public repositories.
    """

    repos_list = []

    for repo in java_repos:
        repos_list.append({
            'ID': repo.id,
            'Name': repo.name,
            'FullName': repo.full_name,
            'URL': repo.html_url,
        })

    # Convert list to DataFrame
    repos_df = pd.DataFrame(repos_list)
    return repos_df

if __name__ == "__main__":
    get_repo_details()