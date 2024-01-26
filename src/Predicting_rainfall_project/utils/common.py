import os
from pathlib import Path
from Predicting_rainfall_project import logger

import yaml
#pythonbox- it will use to convert a dictionary to object(ConfigBox type)
from box import ConfigBox
from box.exceptions import BoxValueError

# a decorator to be used on func and raise ensureError if any,
from ensure import ensure_annotations


@ensure_annotations
def read_yaml(yaml_file_path):
    '''read yaml file and return.

    args: yaml_file_path(str) : path like input

    raise: ValueError: if yaml file is empty
           e: empty file

    return:
        ConfigBox: ConfigBoxType
    '''
    try:
        with open(yaml_file_path, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.debug(f"yaml_file: {yaml_file_path} is successfully loaded")
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(list_of_file_path: list):
    '''create list of directories

    Args:
        path_to_directories (list): list of path of directories
    '''
    # check whether the directory exists or not
    for file_path in list_of_file_path:
        dir_name = Path(file_path)
        os.makedirs(dir_name,exist_ok= True)
        logger.debug(f'{dir_name} is made at {file_path}')
    
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    Args:
        path (Path): path of the file
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"size of the file is : {size_in_kb} KB"

