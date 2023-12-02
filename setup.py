import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = 'MLOPS-Project-with-MLFlow'
AUTHOR_USERNAME = 'Tayyab-R'
SRC_REPO = 'mlops-project-with-mlflow'
AUTHOR_EMAIL = 'riaztayyab212@gmail.com'

setuptools.setup(
    name=f"{REPO_NAME}-{AUTHOR_USERNAME}",
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ML app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker" : f"https://github.com{AUTHOR_USERNAME}/{REPO_NAME}/issues",
        },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),

    )     
    