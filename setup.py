# this script is meant to be part of a Python project's distribution and packaging setup.
## It allows the project to be easily distributed and installed using tools like "pip".

import setuptools

#Read README.md for long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Package Information
__version__ = "0.0.0"

REPO_NAME = "Predicting_rain"
AUTHOR_USER_NAME = "SharmisthaKundu98"
SRC_REPO = "Predicting_rainfall_project"
AUTHOR_EMAIL = "ksharmi1998@gmail.com"

# providing metadata about the package and its distribution
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
