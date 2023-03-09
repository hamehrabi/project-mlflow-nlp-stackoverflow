# Project: MLflow NLP for Tags Classification (Database: StackOverflow)

* data is available at - [this googele drive link](https://drive.google.com/file/d/13A0RtvZZanHXKZNbz5JKwjjO2FedNQCR/view?usp=sharing)

## STEPS -

### STEP 01- Create a repository by using template repository

### STEP 02- Clone the new repository

### STEP 03- Create a conda environment after opening the repository in VSCODE

```bash
conda create --prefix ./env python=3.8 -y
```

```bash
conda activate ./env
```
OR
```bash
source activate ./env
```

### One shot create and activate environment
```bash
conda create --prefix ./env python=3.8 -y && source activate ./env
```

### STEP 04- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 05- initialize the dvc project
```bash
dvc init
```

### STEP 06- commit and push the changes to the remote repository


### extra commands - 

```bash
echo "*.log" >> logs/.gitignore
```

```bash
git rm --cached logs/running_logs.log
```

###  start mlflow sqlite server
```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 127.0.0.1 -p 5000
```