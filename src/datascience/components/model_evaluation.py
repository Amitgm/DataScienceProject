
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from mlflow.sklearn import log_model
from urllib.parse import urlparse
import pandas as pd
import joblib
import mlflow
import mlflow.sklearn
import numpy as np

from src.datascience.utils.common import read_yaml,create_directory,save_json
from src.datascience.constants import *

from src.datascience.entity.config_enitity import ModelEvaluatinconfig



class ModelEvalauation:

    def __init__(self, config: ModelEvaluatinconfig):

        self.config = config

    def eval_metrics(self, actual, pred):

        mse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)


        return mse,mae,r2


    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)

        model = joblib.load(self.config.model_path)


        test_x = test_data.drop(self.config.target_column,axis=1)
        test_y = test_data[self.config.target_column]


        mlflow.set_registry_uri(self.config.mlflow_uri)


        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme


        with mlflow.start_run():


            predictions = model.predict(test_x)

            (rmse,mae,r2) = self.eval_metrics(test_y, predictions)

            scores = {"rmse":rmse, "mae":mae, "r2":r2}

            save_json(path=Path(self.config.metrics_path), data = scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)


        if tracking_uri_type_store!="file":

            mlflow.sklearn.log_model(model,"model",registered_model_name="Elasticmodelnew")
        
        else:

            mlflow.sklearn.log_model(model,"model")
