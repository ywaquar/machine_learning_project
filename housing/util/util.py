"""
This file contains like helper function 
and other reading of yeml file
Means that type of file who has no part in main file of housing.
"""

import yaml
from housing.exception import HousingException
import os,sys
def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and return the content as a dictionary
    file_path:str
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e
    