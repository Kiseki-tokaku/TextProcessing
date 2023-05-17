import os

from setuptools import setup, find_packages

setup(
    name="textprocessing",
    version="0.1",
    description="Text processing package",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    install_requires=[
        "beautifulsoup4==4.12.2",
        "bs4==0.0.1",
        "cleantext==1.1.4",
        "contractions==0.1.73",
        "demoji==1.1.0",
        "en-core-web-sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.5.0/en_core_web_sm-3.5.0-py3-none-any.whl",
        "nltk==3.8.1",
        "numpy==1.24.2",
        "pt-core-news-sm @ https://github.com/explosion/spacy-models/releases/download/pt_core_news_sm-3.5.0/pt_core_news_sm-3.5.0-py3-none-any.whl",
        "spacy==3.5.2",
        "spacy-legacy==3.0.12",
        "spacy-loggers==1.0.4"
        
    ]
)