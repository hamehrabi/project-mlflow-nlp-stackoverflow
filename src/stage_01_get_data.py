import argparse
import os
import logging
from src.utils.common import read_yaml, create_directories, copy_files
import urllib.request as req
from tqdm import tqdm

STAGE = "stage 01 get data" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

## Use the function below, if you use URL links as your data source
# def main(config_path):
#     ## read config files
#     config = read_yaml(config_path)
#     source_data_url = config["source_data_url"]

#     local_data_dir = config["source_download_dir"]["data_dir"]
#     create_directories([local_data_dir])

#     data_filename = config["source_download_dir"]["data_file"]
#     local_data_filepath = os.path.join(local_data_dir, data_filename)

#     logging.info("Download started")
#     filename, headers = req.urlretrieve(source_data_url, local_data_filepath)
#     logging.info(f"Download completed")
#     logging.info(f"Download file is present at: {filename}")
#     logging.info(f"Download headers: \n{headers}")


## Use the function below if you have already downloaded the dataset and the data source is located on your local PC.
def main(config_path: str) -> None:
    """get the image data from source to the present working directory

    Args:
        config_path (str): path to config file
    """
    config = read_yaml(config_path)

    source_data_dirs = config["source_data_dirs"]
    local_data_dirs = config["local_data_dirs"]

    N = len(source_data_dirs)
    for source_data_dir, local_data_dir in tqdm(
        zip(source_data_dirs, local_data_dirs),
        total=N,
        colour="red",
        desc="copying directory:",
    ):
        create_directories([local_data_dir])
        copy_files(source_data_dir, local_data_dir)

    logging.info(f"Copied file is present at: {local_data_dirs}")



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e