# To create a new environment
conda create --prefix ./env python=3.8 -y 
# To activate our environment using the .sh file, we need to determine the location of conda.sh.
source C:/Users/Mehrnaz/anaconda3/etc/profile.d/conda.sh 
# To actvate our environment
source activate ./env
# To install our libraries included in the requirements.txt file
pip install -r requirements.txt
# To export conda.yaml file that we need it for runnign mlflow
conda env export > conda.yaml