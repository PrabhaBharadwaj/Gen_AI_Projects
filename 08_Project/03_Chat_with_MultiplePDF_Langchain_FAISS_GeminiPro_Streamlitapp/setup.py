# It helps to convert src folder's **helper.py** and vectore_store_index.py files as package/internal library
from setuptools import find_packages, setup

setup(
    name="Generative AI Project",
    version="0.0.0",
    author="Prabha Bharadwaj",
    author_email="prabha.m17@gmail.com",
    packages=find_packages(),
    install_requires=[],
)