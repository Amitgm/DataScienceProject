# common functionalities for entire project
import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:

    """
    read yaml file

    Args: 
        path_to_yaml: path to yaml file

    Raises:

        ValueError: if the yaml file is not valid
        e: empty yaml file

    Returns:

        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:

            content = yaml.safe_load(yaml_file)


            # good for yaml file coming in key value pair format    

            logger.info(f"yaml file : {path_to_yaml} loaded successfully")

            print("the content is : {content}, for yaml file : {yaml_file}")

            return ConfigBox(content)
        
    # good exception to use when reading yaml file,use this for only yaml file
    except BoxValueError:

            raise ValueError(f"yaml file is empty")
    
    except Exception as e:
        
        raise e
    

@ensure_annotations
def create_directory(path_to_directory: list, verbose=True):
     
     '''
     Creates a list of directories

     Args:
        path_to_directory: list of directories to be created
        ignore_log (bool,optional): ignore if multiple dirs is to be created
     
     '''
     for path in path_to_directory:
          
        os.makedirs(path, exist_ok=True)

        if verbose:

            logger.info(f"directory : {path} created successfully")

@ensure_annotations
def save_json(path: Path, data: dict):
     
    '''
        save json data

        Args:
            path (Path): path to json file
            data (dict): data to be saved in json file


    '''

    with open(path, "w") as f:
          
        json.dump(data, f)

    logger.info(f"json file : {path} saved successfully")


@ensure_annotations
def load_json(path: Path):
     
    '''
        save json data

        Args:
            path (Path): path to json file
            data (dict): data to be saved in json file
    '''

    with open(path) as f:
          
        content = json.load(f)

    logger.info(f"json file : {path} saved successfully")

    return ConfigBox(content)

@ensure_annotations
def save_model(data: Any, path: Path):

    '''
    save binary file
    Args:
        data: data to be saved as binary
        path: path to save binary file
    
    '''
    joblib.dump(data, path)

    logger.info(f"binary file saved at {path}")



@ensure_annotations
def load_bin(data: Any, path: Path):

    '''
    save binary file
    Args:
        data: data to be saved as binary
        path: path to save binary file
    
    '''
    data = joblib.load(path)

    logger.info(f"binary file loaded from {path}")

    return data




