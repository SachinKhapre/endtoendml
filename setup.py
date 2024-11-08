from setuptools import find_packages, setup
from typing import List

HYPHEN_EDOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    Returns the lisy of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n"," ") for req in requirements]

        if HYPHEN_EDOT in requirements:
            requirements.remove(HYPHEN_EDOT)
            

setup(
    name='mlproject',
    version='0.0.1',
    author='Sachin',
    author_email='khapresachin1010@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)