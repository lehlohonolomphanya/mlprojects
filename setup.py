## create ML pipeline as a package

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''


setup(
name = 'mlproject',
version='0.0.1',
author='Lehlohonolo',
author_email='ephraimhlony@gmail.com',
packages=find_packages(),
install_requires = ['pandas', 'numpy', 'seaborn']
)