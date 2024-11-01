
import os
import pandas as pd
import urllib.request as request
import zipfile
from src.datascience.entity.config_enitity import DataTransformationconfig

from sklearn.model_selection import train_test_split

from src.datascience import logger

class DataTransformation:

    def __init__(self,config:DataTransformationconfig):

        self.config = config

    # downloading the zip file
    def train_test_split(self) -> bool:

        data = pd.read_csv(self.config.data_path)

        train,test = train_test_split(data,test_size=0.2)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info(f"train test split complete")

        logger.info(f"train shape {train.shape}")
        logger.info(f"test shape {test.shape}")

        