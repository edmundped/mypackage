from distutils.command import install_data
from xml.etree.ElementPath import find
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(exclude=["tests*"]),
    license="MIT",
    description="Example python package",
    long_description=open("README.md").read(),
    install_requires=['numpy'],
    url="https:github.com/edmundped/mypackage",
    author="Edmund Dotsey",
    author_email="edmundped@gmail.com"
)