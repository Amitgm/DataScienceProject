import os
from pathlib import Path
import logging
# logging.basicConfig(level=logging.INFO)

project_name = "datascience"

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')


list_of_files = [

    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    # you can call any libraries or packages here
    f"src/{project_name}/components/__init__.py",
    # A generic function that is to be used in entire project
    f"src/{project_name}/utils/__init__.py",
    # functionalities common to entire project
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_enitity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/reserach.ipynb",
    "templates/index.html",
    "app.py",
] 

#  can be implemente in linux , mac machine, windows,
for file_path in list_of_files:

    files_path = Path(file_path)

    filedir,file_name = os.path.split(files_path)

    # if file directory is not there ex : params.yaml

    if filedir != "":

        os.makedirs(filedir, exist_ok=True)

        logging.info(f"created directory : {filedir} for the file : {file_name} ")

    if  (not os.path.exists(files_path))  or (os.path.getsize(files_path) == 0 ):

        with open(files_path, "w") as f:

            pass

            logging.info(f"created empty file : {file_name} ")

    else:

            logging.info(f"file : {file_name} already exists ")









