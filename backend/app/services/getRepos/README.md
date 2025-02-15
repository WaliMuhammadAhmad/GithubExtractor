# Get Details of Public Java Repositories

This dir contains a python script and data related to fetching and analyzing public Java repositories from GitHub. The main work is in python script which extracts repository details using the GitHub Access Token and exports the data to CSV files.

## Contents

- `.env` - Have the **Github Access Token**. You can get your own Personal Github Access Token from [here](https://github.com/settings/tokens).
- `access_token.py` - Script to load retrieve the GitHub access token. You can use the `auth()` in any script/notebook from this script.
- `Java_Public_Repositories.py` - Python script that fetches the latest Java repositories **(since 01-01-2024)** from GitHub using the `PyGitHub` package. The data is processed and exported to CSV file.
- `data` - This folder contains the CSV files exported from `Java_Public_Repositories.py`.

## Overview

Before get starting install dependencies from `requirements.txt` into a virtual environment. Create a virtual environment, activate it and then run this into your terminal:
```bash
pip install -r requirements.txt
```

### access_token.py

This script uses the `dotenv` package to load the GitHub access token in the `.env` file. If your token is valid then this should print your Github Account Name. Here is a highlight of the code:

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

### Java_Public_Repositories.py

- Uses the `PyGitHub` package to interact with the GitHub API.
- Fetches details of Java repositories created after 01-01-2024. This is just done by `query = "language:java created:>=2024-01-01"`. You can change this to get any kind of result.
- Processes the data into a DataFrame.
- Exports the DataFrame to CSV files.

### data dir

```plaintext
data/
├── data_info.csv
└── RepoData.csv
```

The CSV files contain the following columns:

- `ID` - The Project ID of the repository. This is *unique* for every repository on Github.
- `Name` - The name of the repository.
- `FullName` - The full name *(including the owner's username)* of the repository.
- `URL` - The *HTML URL* to the repository.