from setuptools import find_packages, setup
from typing import List

E_DOT = "-e ."

def get_requirements(filePath:str)->List[str]:
    '''
    This function returns the list of requirements from the specified file path.
    '''
    requirements = []
    with open(filePath) as file:
        requirements = file.readlines()
        [requirement.replace("\n", "") for requirement in requirements]

        if E_DOT in requirements:
            requirements.remove(E_DOT)
    
    return requirements

setup(
    name = "mlProject",
    version = "0.0.1",
    auther = "Jack Killelea",
    author_email= "***",
    packages=find_packages(),
    install_requirements=get_requirements("requirements.txt")
)