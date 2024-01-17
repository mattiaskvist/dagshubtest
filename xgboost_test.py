# Load environment variables
from dotenv import load_dotenv
load_dotenv()

import os
repo_name_var = os.getenv("DAGSHUB_REPO_NAME")
repo_owner_var = os.getenv("DAGSHUB_REPO_OWNER")
tracking_uri_var = os.getenv("MLFLOW_TRACKING_URI")
dagshub_token_var = os.getenv("DAGSHUB_TOKEN")
dagshub_username_var = os.getenv("DAGSHUB_USERNAME")

os.environ['MLFLOW_TRACKING_USERNAME'] = dagshub_username_var
os.environ['MLFLOW_TRACKING_PASSWORD'] = dagshub_token_var

# Set up Dagshub and MLflow
import dagshub
import mlflow

dagshub.init(repo_owner=repo_owner_var, repo_name=repo_name_var, mlflow=True)
mlflow.set_tracking_uri(tracking_uri_var)
with mlflow.start_run():
    # Load libraries
    from numpy import loadtxt
    from xgboost import XGBClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

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
    model = XGBClassifier()
    model.fit(X_train, y_train)

    # make predictions for test data
    y_pred = model.predict(X_test)
    predictions = [round(value) for value in y_pred]

    # evaluate predictions
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))

    mlflow.log_param('accuracy', accuracy)
    mlflow.log_metric("metric name", 1)
    mlflow.log_artifact("xgboost_test.py")

    mlflow.end_run()