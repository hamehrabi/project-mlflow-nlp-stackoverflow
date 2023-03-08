import mlflow
import mlflow.sklearn
import argparse

def main():
    #mlflow.set_tracking_uri("http://127.0.0.1:1234")

    with mlflow.start_run() as active_run:
        # print("Launching 'Downloading data'")
        # mlflow.run(".","stage_01", env_manager="local")

        print("Launching 'Data prepration'")
        mlflow.run(".","stage_01", env_manager="local")
        
        print("Launching 'Featurization'")
        mlflow.run(".", "stage_02", env_manager="local")
        
        print("Launching 'Training'")
        mlflow.run(".", "stage_03", env_manager="local")

        print("Launching 'Evaluation'")
        mlflow.run(".", "stage_04", env_manager="local")

if __name__ == '__main__':
    main()