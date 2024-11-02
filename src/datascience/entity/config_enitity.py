# entity all the data classes related stuff
from dataclasses import dataclass
import os
from pathlib import Path
import urllib.request as request
from src.datascience import logger
import zipfile

# no need self keypwrds
@dataclass
class DataIngestionconfig:

    root_dir:Path 
    source_url : str
    local_data_file: Path
    unzip_dir: Path


@dataclass
class DataValidationconfig:

    root_dir : Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict


@dataclass
class DataTransformationconfig:

    root_dir : Path
    data_path : Path

@dataclass
class ModelTrainerConfig:

    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_path: str
    alpha: float
    l1_ratio: float
    target_col: str