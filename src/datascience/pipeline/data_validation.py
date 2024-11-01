
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience.components.data_validation import DataValidation
from src.datascience import logger

stage_name = "DATA_VALIDATION_PIPELINE"


class DataValidationPipeline:

    def __init__(self):

        pass
    
    def initiate_validation_pipeline(self):

        config = ConfigurationManager()



        data_validation_config = config.get_data_validation_config()

        data_validation = DataValidation(config = data_validation_config)

        data_validation.validate_all_columns()


        # config = ConfigurationManager()

    # data_validation_config = config.get_data_validation_config()

    # data_validation = DataValidation(data_validation_config)

    # data_validation.validate_all_columns()



