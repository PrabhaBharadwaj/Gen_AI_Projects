# This setup.py helps to treat some of the subfolders to call as library and helps to do import in main.py

# find_packages(): This helps to look for the constructor file. In this case __init__.py .
# In every folder it makes to look for the constructor file __init__.py
# Where this constructore file available, that folder will be treated as local package for this application
# In this case __init__.py is there inside src folder. so this allowes to write ""from src.helper import *"
# So this import statement helps to read all function or variable written inside src folders any file as Global func or variable
# Inside requirements.txt --> -e .  #This is to install the setup.py as library and install all which mentioned inside setup.py

from setuptools import find_packages, setup

setup(
    name="Generative AI Project",  # Name of the  application/our local package name when we install -e. in requirements.txt
    version="0.0.0",
    author="Prabha",
    author_email="prabha.m17@gmail.com",
    packages=find_packages(),
    install_requires=[],
)
