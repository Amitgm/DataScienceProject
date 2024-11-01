# componenets is class data ingestion
import os
import pandas as pd
import urllib.request as request
import zipfile
from src.datascience.entity.config_enitity import DataIngestionconfig

from src.datascience import logger

class DataIngestion:

    def __init__(self,config:DataIngestionconfig):

        self.config = config

    # downloading the zip file
    def download_file(self):

        if not os.path.exists(self.config.local_data_file):
            # retrieving the source_url and then saving it in the local data file
            filename, headers = request.urlretrieve(self.config.source_url,self.config.local_data_file)


            logger.info(f"downloaded file from {self.config.source_url} to {self.config.local_data_file}")

        else:
            logger.info(f"file already exists")

    
    def extract_zip_file(self):

        '''
        
        zip_file_path = str
        extracts zip file into the given directory

        '''

        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir,exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:


            zip_ref.extractall(unzip_dir)