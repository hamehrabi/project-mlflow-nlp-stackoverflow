import os
import yaml
import logging
import pandas as pd
import json
import shutil
from tqdm import tqdm
import time

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"yaml file: {path_to_yaml} loaded successfully")
    return content

def create_directories(path_to_directories: list) -> None:
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logging.info(f"created directory at: {path}")


def save_json(path: str, data: dict) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")

def get_df(path_to_data: str, sep: str="\t") -> pd.DataFrame:
    df = pd.read_csv(
        path_to_data, 
        encoding="utf-8",
        header=None,
        delimiter=sep,
        names=["id", "label", "text"]
    )
    logging.info(f"The input data frame {path_to_data} size is {df.shape}\n")
    return df

def copy_files(source_data_dir: str, local_data_dir: str) -> None:
    """Copies file from source to destination directory

    Args:
        source_data_dir (str): source data directory
        local_data_dir (str): local data directory
    """
    list_of_files = os.listdir(source_data_dir)
    N = len(list_of_files)

    for filename in tqdm(
        list_of_files,
        total=N,
        desc=f"copying file from {source_data_dir} to {local_data_dir}",
        colour="green",
    ):
        src = os.path.join(source_data_dir, filename)
        dest = os.path.join(local_data_dir, filename)
        shutil.copy(src, dest)

    logging.info(
        f"all the files has been copied from {source_data_dir} to {local_data_dir}"
    )