from setuptools import setup, find_packages
#Declaring variables for setup function
PROJECT_NAME='housing-predictor'
VERSION="0.0.4"
AUTHOR='Waquar'
DESCRIPTION="This is first Machine Learning End to End Project"

REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list():
    """
    Description: This fynction is going to return list of requirement
    mentioned in requirements.txt file

    return This function is going to return a list which contaion name
    of libraries mentioned in requirements.txt file
    """

    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")
        
setup(
name =PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()
)