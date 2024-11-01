
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience import logger

stage_name = "DATA_INGESTION_PIPELINE"


class DataIngestionPipeline:

    def __init__(self):

        pass
    
    def initiate_ingestion_pipeline(self):

        config = ConfigurationManager()

        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(config = data_ingestion_config)

        data_ingestion.download_file()

        data_ingestion.extract_zip_file()


if __name__ == "__main__":

    try:

        logger.info(f"Starting pipeline {stage_name}")

        data_ingestion = DataIngestionPipeline()

        data_ingestion.initiate_ingestion_pipeline()

        logger.info(f"Finished pipeline {stage_name}")

    except Exception as e:

        logger.exception(f"Exception occurred in pipeline {stage_name}")

        raise e

