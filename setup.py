###from distutils.version import Version
from setuptools import setup, find_packages
from typing import List


#Declaring variable for a setup function

PROJECT_NAME="housing-predictor"
VERSION="0.0.2"
AUTHOR= "Akash"
DISCRIPTION= "First project of machine learning"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"
def get_requirements_list()->List[str]:

    '''
    Description:This function is going to return list of requirement

    mention in requirements.txt file

    return This function is going to return a list which contain name of the libraries

    '''

    with open (REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(  
name =PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DISCRIPTION,
packages= find_packages(),
install_requires=get_requirements_list()


)

