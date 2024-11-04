# all the configuration file goes here
from src.datascience.utils.common import read_yaml,create_directory,save_json
from src.datascience.constants import *
from src.datascience.entity.config_enitity import DataIngestionconfig,DataValidationconfig,DataTransformationconfig,ModelTrainerConfig,ModelEvaluatinconfig
import os


# os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/amittimer/DataScienceProject.mlflow"
# os.environ["MLFLOW_TRACKING_USERNAME"] = "amittimer"
# os.environ["MLFLOW_TRACKING_PASSWORD"] = "2f89005b2e2d95e60f8bd873d4818a02bad814f6"

# updating the configuration manager
class ConfigurationManager:

    def __init__(self,config_filepath=CONFIG_FILE_PATH,
                 param_file_path=PARAMS_FILE_PATH,
                 schema_file_path=SCHEMAS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.param = read_yaml(param_file_path)
        self.schema = read_yaml(schema_file_path)


        create_directory([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionconfig:


        config = self.config.data_ingestion

        create_directory([config.root_dir,config.unzip_dir])

        data_ingestion_config = DataIngestionconfig(


            root_dir=Path(config.root_dir),
            source_url=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=config.unzip_dir

        )

        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationconfig:


        config = self.config.data_validation
        # we are getting all the columns from the schema file
        schema = self.schema.COLUMNS

        create_directory([config.root_dir])

        print("the config",config)

        print("unzip data",config.unzip_data_dir)

        data_validation_config = DataValidationconfig    (


            root_dir=Path(config.root_dir),
            STATUS_FILE = config.STATUS_FILE,
            unzip_data_dir =Path(config.unzip_data_dir),
            all_schema = schema

        )

        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformationconfig:


        config = self.config.data_transformation
       

        create_directory([config.root_dir])

        data_transformation_config = DataTransformationconfig    (

            root_dir=Path(config.root_dir),
            data_path =Path(config.data_path),
    
        )

        return data_transformation_config
    

    def get_model_trainer(self) -> ModelTrainerConfig:

        

        config = self.config.model_trainer
        # we are getting all the parameters

        params = self.param.ElasticNet

        schema = self.schema.TARGET_COLUMN
        

        create_directory([config.root_dir])

        # creating the object with all the class attributes/members/parameters

        model_trainer_config = ModelTrainerConfig    (


            root_dir = config.root_dir,
            train_data_path= config.train_data_path,
            test_data_path = config.test_data_path,
            model_path=config.model_path,
            alpha = params.alpha,
            l1_ratio = params.l1_Ratio,
            target_col = schema.name,

        )

        # returning the object
        return model_trainer_config
    

    def get_model_evaluation_config(self) -> ModelEvaluatinconfig:

        config = self.config.model_evaluation

        params = self.param.ElasticNet

        schema = self.schema.TARGET_COLUMN

        create_directory([config.root_dir])


        modelevaluationconfig =  ModelEvaluatinconfig(
            root_dir = config.root_dir,
            model_path = config.model_path,
            test_data_path = config.test_data_path,
            all_params = params,
            metrics_path = config.metrics_path,
            target_column = schema.name,
            mlflow_uri= os.environ['MLFLOW_TRACKING_URI']
        )


        return modelevaluationconfig
    



