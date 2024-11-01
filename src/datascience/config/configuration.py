# all the configuration file goes here
from src.datascience.utils.common import read_yaml,create_directory
from src.datascience.constants import *
from src.datascience.entity.config_enitity import DataIngestionconfig,DataValidationconfig,DataTransformationconfig

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

