
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger
from pathlib import Path

stage_name = "DATA_TRANSFORMATION_PIPELINE"


class DataTransformationPipeline:

    def __init__(self):

        pass
    
    def initiate_transformation_pipeline(self):
        #  run this code if validation status is true
        try:
            with open(Path("artifacts/data_validation/status.txt"),"r") as f:

                status = f.read().split(" ")[-1]

                print("status",status)
            
            if status == 'True':

                config = ConfigurationManager()

                data_transformation_config = config.get_data_transformation_config()

                data_transformation = DataTransformation(config = data_transformation_config)

                data_transformation.train_test_split()

            else:

                raise Exception("data scheme is not valid")
            
        except Exception as e:

            print(e)




        # config = ConfigurationManager()

    # data_validation_config = config.get_data_validation_config()

    # data_validation = DataValidation(data_validation_config)

    # data_validation.validate_all_columns()



