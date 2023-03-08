import mlflow
import argparse

def main():
    #mlflow.set_tracking_uri("http://127.0.0.1:1234")

    with mlflow.start_run() as run:
        mlflow.run(".", "stage_01")
        mlflow.run(".", "stage_02")
        mlflow.run(".", "stage_03")
        mlflow.run(".", "stage_04")

if __name__ == '__main__':
    main()