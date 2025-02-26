import os
import pandas as pd
from .auth import github
from uuid import uuid4

def get_repo_details(lang: str, query: str = "created:>=2025-01-01", sort: str = 'stars', order: str = 'asc', output_dir: str = 'output') -> str | None:
    """
    Retrieves details of public repositories and exports them to a CSV file.

    Args:
        lang (str): The primary language of the repositories.
        query (str): The query to search for repositories. Defaults to 'created:>=2025-01-01'.
        sort (str): The field to sort by. Options: 'stars', 'forks', 'updated'. Defaults to 'stars'.
        order (str): The sort order. Options: 'asc', 'desc'. Defaults to 'asc'.
        output_dir (str): The directory to save the CSV file. Defaults to 'output'.

    Returns:
        str: The path to the CSV file if successful.
        None: If the retrieval fails.
    """
    try:
        g, token = github()
        if g is None:
            print("GitHub authentication failed. Cannot retrieve repositories.")
            return None
        
        print(query)
        repos = g.search_repositories(query=query)
        print(f"{repos.totalCount} repositories found!")

        data = extract(repos)
        
        os.makedirs(output_dir, exist_ok=True)
        id = uuid4()
        filename = f'{lang}-repos-{id}.csv'
        filepath = os.path.join(output_dir, filename)
        data.to_csv(filepath, index=False)
        print(f'Repositories data saved successfully @ {filepath}!')
        return filepath
    
    except Exception as e:
        print(f"Failed to retrieve the repositories! Error: {str(e)}")
        return None

def extract(repos) -> pd.DataFrame:
    """
    Extracts details from a list of repositories and returns them as a DataFrame.

    Args:
        repos: A PaginatedList of repositories returned by the GitHub API.

    Returns:
        pd.DataFrame: A DataFrame containing repository details.
    """
    repos_list = []

    for repo in repos:
        repos_list.append({
            'ID': repo.id,
            'Language': repo.language,
            'Owner': repo.owner.login,
            'Name': repo.name,
            'FullName': repo.full_name,
            'Description': repo.description if repo.description else None,
            "Topics": repo.topics,
            'Default Branch': repo.default_branch,
            'HTMLURL': repo.html_url,
            'GitURL': repo.git_url,
            'SSHURL': repo.ssh_url,
            'CloneURL': repo.clone_url,
            "HomePage": repo.homepage,
            'Size (KB)': repo.size,
            'Stars': repo.stargazers_count,
            'Forks': repo.forks_count,
            'Watchers': repo.watchers_count,
            'OpenIssues': repo.open_issues_count,
            'NetworkCount': repo.network_count,
            'Subscribers': repo.subscribers_count,
            'Archived': repo.archived,
            'Template': repo.is_template,
            'License': repo.license.name if repo.license else None,
            'CreatedAt': repo.created_at,
            'UpdatedAt': repo.updated_at,
            'LastModified': repo.last_modified_datetime,
        })

    return pd.DataFrame(repos_list)

if __name__ == "__main__":
    get_repo_details("python")  # Added argument for lang