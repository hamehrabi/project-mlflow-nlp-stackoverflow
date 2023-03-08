from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "AIOps-project-mlflow-NLP-usecase"
AUTHOR_USER_NAME = "Hamed Mehrabi"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for mlfow-NLP usecase",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/hamehrabi/project-mlflow-nlp-stackoverflow",
    author_email="mehrabi.hamed@outlook.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.8",
    install_requires=LIST_OF_REQUIREMENTS
)
