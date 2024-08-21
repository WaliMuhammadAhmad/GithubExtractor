# Get Details of Public Java Repositories

This dir contains a notebook and data related to fetching and analyzing Java public repositories from GitHub. The main work is in notebook which extracts repository details using the GitHub API using the  and exports the data to CSV files.

## Contents

- `.env` - Have the **Github Access Token**. You can get your own Personal Github Access Token from [here](https://github.com/settings/tokens).
- `access_token.py` - Script to load retrieve the GitHub access token just for validating. From this code you can use the access token in any script/notebook.
- `Java_Public_Repositories.ipynb` - Jupyter notebook that fetches the latest Java repositories **(as of 01-01-2024)** from GitHub using the PyGitHub package. The data is processed and exported to CSV files.
<!-- - `RepoData2023.csv` - CSV file containing repository data for the year 2023. Total 1020 entries -->
- `RepoData.csv` - CSV file containing repository data for the year 2024. Total **1021** entries. 
<!-- - `TopRepoData.csv` - CSV file containing data for the top Java repositories. Total **1020** entries.  -->

## Overview

### access_token.py

This script uses the `dotenv` package to load the GitHub access token in the `.env` file. If your token is valid then this should print your Github Account Name.

Here is a highlight of the code:

```python
load_dotenv()
github_token = os.getenv("GITHUB_TOKEN")

try:
    auth = Auth.Token(github_token)
    g = Github(auth=auth)
    usr = g.get_user()
    print(usr.name)
except:
    print(f'[{github_token}] is not valid')
```

### Java_Public_Repositories.ipynb

- Uses the `PyGitHub` package to interact with the GitHub API.
- Fetches details of Java repositories created after 01-01-2024. This is just done by `query = "language:java created:>=2024-01-01"`. You can change this to get any kind of result.
- Processes the data into a DataFrame.
- Exports the DataFrame to CSV files.
- I highly recommend running this notebook on **Google Colab**. This notebook is aligned with google colab and work better on its environment. *You'll see how!*

### CSV Files

The CSV files contain the following columns:

- `ID` - The Project ID of the repository. This is *unique* for every repository on Github.
- `Name` - The name of the repository.
- `FullName` - The full name *(including the owner's username)* of the repository.
- `URL` - The *HTML URL* to the repository.