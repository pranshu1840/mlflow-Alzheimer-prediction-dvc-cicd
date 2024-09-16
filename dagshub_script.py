import dagshub
dagshub.init(repo_owner='pranshu1840', repo_name='mlflow-cancer-prediction-dvc-cicd', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)