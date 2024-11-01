import os
import pandas as pd

from src.datascience.entity.config_enitity import DataValidationconfig


class DataValidation:

    def __init__(self,config:DataValidationconfig):

        self.config = config

    # downloading the zip file
    def validate_all_columns(self) -> bool:

        try:

            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)

            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            all_data_types = self.config.all_schema.values()


            print("all schemas",self.config.all_schema)

            # verifying the schema is correct or not with all columns
            for col in all_cols:

                if col not in all_schema and col.dtype != self.config.all_schema[col]:

                    validation_status = False

                    with open(self.config.STATUS_FILE,"w") as f:

                        f.write(f"failed {validation_status}" )

                else:
                    validation_status = True

                    with open(self.config.STATUS_FILE,"w") as f:

                        f.write(f"Validation status: {validation_status}" )

            return validation_status 
        
        except Exception as e:

            raise e