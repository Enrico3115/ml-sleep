import os
import glob
import pandas as pd
from dotenv import load_dotenv

# Securely load the token from the .env file before importing Kaggle
load_dotenv()

from kaggle.api.kaggle_api_extended import KaggleApi

def fetch_and_load_data(dataset="samartalwar/sleep-debt-and-screen-time-late-night-phone-habits",
                        data_dir="../data"):
    os.makedirs(data_dir, exist_ok=True)

    print("Authenticating and downloading dataset...")
    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(dataset, path=data_dir, unzip=True)

    csv_files = glob.glob(f"{data_dir}/*.csv")

    if not csv_files:
        raise FileNotFoundError("No CSV file found after download.")

    print(f"Loading {csv_files[0]}...")
    return pd.read_csv(csv_files[0])