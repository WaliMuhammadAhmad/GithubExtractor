# Push the dataset to HuggingFace

This folder containes the python script/Notebook to push the dataset on huggingface. This includes, first validating the huggingface access token `HF_TOKEN`, creating a new dataset repository on huggingface and clone it into local codespace, then place all the dataset into that repository and push then to huggingface using legacy `git` method because believe me it's immune to internet connection and won't give you connection error.

## Content

- `.gitignore` - Specifies files and directories to be ignored. Open it to see the content!

- `access_token.py` - Script to load retrieve the huggingface access token. You can use the `auth()` in any script/notebook from this script.

- `get_repo.py` - This script authenticates the user with huggingface, creates and retrieves a repository, and clones it locally.

- `push.py` -  This script authenticates the user and pushes local directories to a huggingface repository.

- `push_to_hf.ipynp` - Notebook alternative to push.py file. Made to run on **Google Colab**.

## Overview

Mostly the scripts uses `huggingface_hub` package to start the process. To start the process, install dependencies from `requirements.txt` into a virtual environment. Create a virtual environment, activate it and then run this into your terminal:
```bash
pip install -r requirements.txt
```

 `loggings.py` is used in every script for creating logs. All of the logs are placed in `./log` dir by default.

### access_token.py

To authenticate, use the `auth()` function from access_token.py. This script will handle the retrieval of your Hugging Face access token.

### get_repo.py

This script aligns the process of creating or retrieving a Hugging Face dataset repository. It first authenticates the user, then attempts to create a new dataset repository (if it doesn’t already exist) and clones it locally.

### push.py

The push.py script handles the process of pushing your dataset to a Hugging Face repository. After authenticating the user, it moves the necessary directories to the cloned repository and commits the changes using the legacy git method. This method is preferred for its reliability, especially in environments with unstable internet connections. It also logs every step of the process for easy debugging.

### push_to_hf.ipynp

Alternatively, use the notebook on colab to mimic the process of `push.py`. This is recommend if you don't have a good internet. Just zip all the dataset and push it to colab (zipping significantly reduces the size) and from their unzip the dataset zip file and push it to huggingface. Easy peasy!

### loggings.py

Logging is provided by `loggings.py` to help track the operations performed by each script. It creats a `./log` dir in codespace and places all the logs from other scripts there. The logs statuses `[info, warning, error]` are according to state. 