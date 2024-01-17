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
mlflow.set_experiment("multiclass_test")
with mlflow.start_run() as run:
    import xgboost as xgb
    import pandas as pd
    from sklearn.model_selection import train_test_split    
    from xgboost import XGBClassifier
    from sklearn.metrics import accuracy_score, recall_score, precision_score, classification_report
 
    # Load data
    data = pd.read_csv("winequality-red.csv")
    
    # Separate target variable
    X = data.drop('quality', axis=1)
    y = data['quality'] - data['quality'].min()

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create an instance of the XGBClassifier
    model = XGBClassifier(objective='multi:softprob')

    # Fit the model to the training data
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred, average='weighted')
    precision = precision_score(y_test, y_pred, average='weighted')
    
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    print("Recall: %.2f%%" % (recall * 100.0))
    print("Precision: %.2f%%" % (precision * 100.0))
    print(classification_report(y_test, y_pred))
    
    run_id = run.info.run_id
    
    mlflow.end_run()

    # Log own metrics and artifacts
    MlflowClient().log_artifact(run_id, 'multiclass_test.py')
    