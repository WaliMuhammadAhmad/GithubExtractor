# Initial Scraper which didn't worked

This folder contains scripts and notebooks designed to extract Java methods and their corresponding test cases from GitHub repositories. The extraction process is automated and utilizes the `javalang` package to parse Java files. This scraper is working fine, but it did't work fine.

## Contents

- `Dataset[Colab_Version].ipynb`: A Jupyter Notebook designed for use in **Google Colab**. It automates the process of cloning GitHub repositories, extracting Java methods and test cases, and saving the results in CSV files. The notebook also includes functionality to compress the resulting CSV files into a ZIP archive.
- `Dataset[Kaggle_Version].ipynb`: A Jupyter Notebook similar to the Colab version but designed for use in **Kaggle**. It performs the same tasks, with adjustments made for Kaggle’s codespace, such as different input and output paths etc.
- `data_info.csv`: A CSV file containing information about the GitHub repositories to be cloned and analyzed.
- `requirements.txt`: A file listing the Python dependencies needed to run the notebooks. These include `subprocess`, `pandas`, and `javalang`.

## Installation

Before running the notebooks, install the required Python packages by running:

```bash
pip install -r requirements.txt
```

## How things work in Notebook

**Cloning Repositories**: The notebooks start by reading repository URLs from `data_info.csv` and cloning them into a specified directory.

**Method and Test Case Extraction**: The cloned repositories are then scanned for Java files. The `javalang` package is used to parse these files, extract method declarations, and attempt to match test cases to these methods. The extracted data is saved as CSV files.

**Zipping the Results**: Once the data extraction is complete, the resulting CSV files are compressed into a ZIP file for easy download and storage.

**Output**: The results, including the extracted methods and test cases, are stored in CSV format and can be used for further analysis or machine learning tasks.

## Known Issues

Initially, this scraper was successful in extracting methods and test cases using the `javalang` package. However, it encountered difficulties in accurately mapping test cases to their corresponding methods. This limitation means that while methods and test cases are extracted, they are not reliably paired. The current code and logic can still be used, but it requires fixing to ensure accurate method-to-test-case mapping. *tbh i am waiting for an angel*

*Please fix this issue and you can keep these notebook i really don't want to keep these junk files!*