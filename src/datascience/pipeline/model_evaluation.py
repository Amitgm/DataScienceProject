
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvalauation
from src.datascience import logger

stage_name = "MODEL_EVALUATION_PIPELINE"


class model_evaluation_pipeline:

    def __init__(self):

        pass
    
    def initiate_model_evaluation(self):

        config = ConfigurationManager()

        ModelEvaluatinconfig = config.get_model_evaluation_config()

        Modelevaluation = ModelEvalauation(ModelEvaluatinconfig)

        Modelevaluation.log_into_mlflow()


     

