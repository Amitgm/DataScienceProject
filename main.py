''' BIG NOTE: WHEN IMPORTING MODULES FROM A DIRECTORY, AND IMPORTING A LOGGER DEFINED IN THE __INIT__.PY FILE, THE LOGGER 

MUST BE DEFINED AS logger = logging.getLogger("datasciencelogger") IN __INIT__.PY FILE.'''

from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionPipeline
from src.datascience.pipeline.data_validation import DataValidationPipeline
logger.info("Welcome to our custom logger!")


stage_name = "DATA INGESTION PIPELINE STAGE"

try:

    logger.info(f"Starting pipeline {stage_name}")

    data_ingestion = DataIngestionPipeline()

    data_ingestion.initiate_ingestion_pipeline()

    logger.info(f"Finished pipeline stage {stage_name}")

except Exception as e:

    logger.exception(f"Exception occurred in pipeline {stage_name}")

    raise e

stage_name = "DATA Validation PIPELINE STAGE"

try:

        logger.info(f"Starting pipeline {stage_name}")

        data_validation = DataValidationPipeline()

        data_validation.initiate_validation_pipeline()
        
        logger.info(f"Finished pipeline {stage_name}")

except Exception as e:

        logger.exception(f"Exception occurred in pipeline {stage_name}")

        raise e





