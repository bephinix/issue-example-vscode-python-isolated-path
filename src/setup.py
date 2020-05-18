from setuptools import find_packages, setup

setup(
    name="exampleproject",
    version="0.0.0",
    packages=find_packages(where="src"),
    package_dir={"exampleproject": "src/exampleproject"},
)
