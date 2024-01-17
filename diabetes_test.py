# Load environment variables
from dotenv import load_dotenv
from sklearn.metrics import recall_score
load_dotenv()

import os
repo_name_var = os.getenv("DAGSHUB_REPO_NAME")
repo_owner_var = os.getenv("DAGSHUB_REPO_OWNER")
dagshub_token_var = os.getenv("DAGSHUB_TOKEN")
dagshub_username_var = os.getenv("DAGSHUB_USERNAME")

os.environ['MLFLOW_TRACKING_USERNAME'] = dagshub_username_var
os.environ['MLFLOW_TRACKING_PASSWORD'] = dagshub_token_var

# Set up Dagshub and MLflow
import dagshub
import mlflow
from mlflow.tracking import MlflowClient

dagshub.init(repo_owner=repo_owner_var, repo_name=repo_name_var, mlflow=True)
mlflow.xgboost.autolog(log_input_examples=False, log_datasets=False, log_model_signatures=True, disable=False)
with mlflow.start_run() as run:
    # Load libraries
    from numpy import loadtxt
    from xgboost import XGBClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, recall_score, precision_score

    # load data
    dataset = loadtxt('pima-indians-diabetes.csv', delimiter=",")

    # split data into X and y
    X = dataset[:,0:8]
    Y = dataset[:,8]

    # split data into train and test sets
    seed = 7
    test_size = 0.33
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

    # fit model on training data
    model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
    model.fit(X_train, y_train)

    # make predictions for test data
    y_pred = model.predict(X_test)

    # evaluate predictions
    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)

    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    print("Recall: %.2f%%" % (recall * 100.0))
    print("Precision: %.2f%%" % (precision * 100.0))
    run_id = run.info.run_id

    mlflow.end_run()
    
    # Log metrics
    # Här loggar vi metrics till MLflow. Accuracy, recall och precision loggas automatiskt innan
    MlflowClient().log_artifact(run_id, 'diabetes_test.py')

    