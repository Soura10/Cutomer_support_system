'''
Docstring for setup
from setuptools import setup, find_packages

setup( name="E-cmmerce-bot",
      version="0.0.1",
      author = "Souradeep Roy",
      author_email="souradeeproy.10@gmail.com",
      package= find_packages(include=["data_ingestion","prompt_library","Retriever","utils"],
                             exclude=["data","static","templates","__pycache__","notebook"]),
      install_requires = ["langchain_astradb","langchain"]
      )

      '''

from setuptools import find_packages,setup

setup(name="e-commerce-bot",
       version="0.0.1",
       author="soura",
       author_email="souradeeproy.10@gmail.com",
       packages=find_packages(),
       install_requires=['langchain-astradb','langchain'])