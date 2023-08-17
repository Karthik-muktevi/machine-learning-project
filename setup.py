from setuptools import setup,find_packages
from typing import List


PROJECT_NAME = 'Machine_Learning_Project'
DESCRIPTION = 'This is machine learning project in modular coding'
VERSION = '1.0'
AUTHOR = 'Karthik'
EMAIL = 'dummy@datascience.com'

REQUIREMENTS = 'requirements.txt'
HYPHEN_E_DOT = '-e .'

def get_requirements()->List[str]:
    with open(REQUIREMENTS) as requirements_file:
        requirements_list = requirements_file.readlines()
        requirements_list = [requirement.replace("\n","") for requirement in requirements_list]

        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)

        return requirements_list




setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=EMAIL,
      packages=find_packages(),
      install_requires = get_requirements()
     )