import os
import pandas as pd
from auth import github
from datetime import datetime

def get_repo_details(query="language:java created:>=2025-02-16",sort='stars',order='asc',output_dir='data'):
    """
    Retrieves details of public repositories and exports them to a CSV file.

    Args:
        query (str): The query to search for repositories. Defaults to 'language:java created:>=2025-02-16'.
        sort (str): The field to sort the repositories by. Options ('stars', 'forks', 'updated'). Defaults to 'stars'.
        order (str): The sort order. Options ('asc','desc').  Defaults to 'asc'.
        output_dir (str): The directory to save the CSV file. Defaults to 'data'.

    Returns:
        filepath (str): The path to the CSV file if the retrieval is successful.
        None if the retrieval fails.
    """

    try:
        g, token = github()
        repos = g.search_repositories(query=query,sort=sort,order=order)
        print(f"{repos.totalCount} Java repositories found!")

        data = extract(repos)
        
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'RepoData-{timestamp}.csv'
        filepath = os.path.join(output_dir, filename)
        data.to_csv(filepath, index=False)
        print(f'Repositories data saved successfully @ {filepath}!')
        g.close()
        return filepath
    
    except Exception as e:
        print(f"Failed to retrieve the repositories! \n Error: {str(e)}")
        return None

def extract(repos):
    """
    Extracts details from the list repositories and returns them as a DataFrame.

    Args:
        repos (PaginatedList): A list of repositories returned by the GitHub API.

    Returns:
        repos_df (DataFrame): A DataFrame containing the details of the public repositories.
    """

    repos_list = []

    for repo in repos:
        repos_list.append({
            'ID': repo.id,
            'Language' : repo.language,
            'Name': repo.name,
            'Ower': repo.owner.login,
            'FullName': repo.full_name,
            'Visibility': repo.visibility,
            'HTMLURL': repo.html_url,
            'GitURL': repo.git_url,
            'SSHURL': repo.ssh_url,
            'CloneURL': repo.clone_url,
            'Description': repo.description if repo.description else None,
            'ETAG': repo.etag,
            'Stars': repo.stargazers_count,
            'Forks': repo.forks_count,
            'Watchers': repo.watchers_count,
            'OpenIssues': repo.open_issues_count,
            'NetworkCount': repo.network_count,
            'Subscribers': repo.subscribers_count,
            'Default Branch': repo.default_branch,
            'Size': repo.size,
            'Template': repo.is_template,
            'License': repo.license,
            'CreatedAt': repo.created_at,
            'UpdatedAt': repo.updated_at,
            'LastModified': repo.last_modified_datetime,
        })

    repos_df = pd.DataFrame(repos_list)
    return repos_df

if __name__ == "__main__":
    get_repo_details()